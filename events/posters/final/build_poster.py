import random, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from scipy import ndimage
random.seed(11); np.random.seed(11)
SRC='../../images/11.webp'
orig=Image.open(SRC).convert('RGB'); OW,OH=orig.size
CREAM=(233,212,175); CORAL=(224,64,40); LIME=(194,193,0); DARK=(5,39,25); DARKTXT=(4,28,18)
F={'p500':'font_1.ttf','p600':'font_2.ttf','p700':'font_3.ttf'}
SYM='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; SPARK='✦'
def font(k,s): return ImageFont.truetype(F[k],s)

def upscaled(scale):
    a=orig.resize((int(OW*scale),int(OH*scale)),Image.LANCZOS)
    return a.filter(ImageFilter.UnsharpMask(radius=1.5,percent=60,threshold=2))

def foreground_mask(img):
    L=np.asarray(img.convert('L')).astype(int)
    return np.abs(L-28)>48

def erase_mask(img, scale):
    """mask of the old text block, pills and footer in the lower part of the artwork (side doodles are kept)"""
    fg=foreground_mask(img); H,W=fg.shape
    y0=int(1500*scale); m=np.zeros_like(fg); m[y0:]=fg[y0:]
    lab,n=ndimage.label(m); keep=np.zeros_like(fg)
    for i,sl in enumerate(ndimage.find_objects(lab),1):
        ys,xs=sl; cx=(xs.start+xs.stop)/2; w=xs.stop-xs.start
        if ys.start<=y0: continue                      # touches the polaroid above the region: never erase
        if 300*scale<cx<1330*scale or w>250*scale: keep[lab==i]=True
    keep=ndimage.binary_dilation(keep,iterations=int(7*scale))
    return keep

def band_fill(canvas_np, src_np, need, cell=48):
    """fill 'need' pixels of canvas with grain cells taken from the same vertical band of the source artwork"""
    H,W,_=canvas_np.shape; sh,sw,_=src_np.shape
    src_fg=ndimage.binary_dilation(np.abs(src_np.mean(2)-28)>48,iterations=6)
    bands={}
    for y in range(0,sh-cell,cell//2):
        for x in range(0,sw-cell,cell//2):
            if not src_fg[y:y+cell,x:x+cell].any(): bands.setdefault(y//160,[]).append((x,y))
    bkeys=sorted(bands)
    def nearest_band(y):
        b=y//160
        return min(bkeys,key=lambda k:abs(k-b))
    for y in range(0,H,cell):
        for x in range(0,W,cell):
            sub=need[y:y+cell,x:x+cell]
            if not sub.any(): continue
            # map canvas y to source y (canvas may be offset/extended): clamp into source range
            sy=min(max(y,0),sh-1)
            sx,syy=random.choice(bands[nearest_band(sy)])
            t=src_np[syy:syy+cell,sx:sx+cell]
            k=random.randint(0,3); t=np.rot90(t,k)
            if random.random()<0.5: t=t[:,::-1]
            h,w=sub.shape; t=t[:h,:w]
            region=canvas_np[y:y+h,x:x+w]; region[sub]=t[sub]
    return canvas_np

def rich_parts(txt,fnt):
    sym=ImageFont.truetype(SYM,int(fnt.size*0.9)); parts=[]; buf=''
    for ch in txt:
        if ch in '→✦':
            if buf: parts.append((buf,fnt)); buf=''
            parts.append((ch,sym))
        else: buf+=ch
    if buf: parts.append((buf,fnt))
    return parts
def rich_len(d,txt,fnt): return sum(d.textlength(t,font=f) for t,f in rich_parts(txt,fnt))
def rich_draw(d,x,y,txt,fnt,fill):
    base=fnt.getbbox('Hg')
    for t,f in rich_parts(txt,fnt):
        bb=f.getbbox('Hg'); dy=(base[3]-bb[3]); d.text((x,y+dy),t,font=f,fill=fill); x+=d.textlength(t,font=f)
def text_center(d,cx,y,txt,fnt,fill):
    w=rich_len(d,txt,fnt); rich_draw(d,cx-w/2,y,txt,fnt,fill); return fnt.size
def pill(d,cx,y,txt,fnt,bg,fg,padx,h):
    w=rich_len(d,txt,fnt)+2*padx; d.rounded_rectangle((cx-w/2,y,cx+w/2,y+h),radius=h//2,fill=bg)
    bb=fnt.getbbox('Hg'); th=bb[3]-bb[1]; rich_draw(d,cx-(w-2*padx)/2,y+(h-th)/2-bb[1],txt,fnt,fg); return h
def ribbon(canvas,center,txt,fnt,w,h,angle=-9):
    layer=Image.new('RGBA',(w+80,h+80),(0,0,0,0)); d=ImageDraw.Draw(layer)
    d.rounded_rectangle((40,40,40+w,40+h),radius=18,fill=CORAL+(255,))
    tw=d.textlength(txt,font=fnt); bb=fnt.getbbox(txt)
    d.text((40+(w-tw)/2,40+(h-(bb[3]-bb[1]))/2-bb[1]),txt,font=fnt,fill=CREAM)
    layer=layer.rotate(angle,resample=Image.BICUBIC,expand=True)
    canvas.paste(layer,(int(center[0]-layer.width/2),int(center[1]-layer.height/2)),layer)

def text_block(d,cx,y,scale,spec,pillt,tag,button,footer):
    sc=lambda v:int(v*scale)
    f=font('p700',sc(spec['date_size'])); y+=text_center(d,cx,y,spec['date'],f,CREAM)+sc(5)
    f=font('p600',sc(spec['sub_size'])); y+=text_center(d,cx,y,spec['sub'],f,CORAL)+sc(spec.get('gap1',16))
    f=font('p600',sc(spec['chip_size'])); padx=sc(18); gap=sc(14); h=sc(spec.get('chip_h',44))
    widths=[rich_len(d,c,f)+2*padx for c in spec['chips']]; total=sum(widths)+gap*(len(widths)-1); x=cx-total/2
    for c,w in zip(spec['chips'],widths):
        d.rounded_rectangle((x,y,x+w,y+h),radius=h//2,fill=CREAM)
        bb=f.getbbox('Hg'); rich_draw(d,x+padx,y+(h-(bb[3]-bb[1]))/2-bb[1],c,f,DARKTXT); x+=w+gap
    y+=h+sc(spec.get('gap2',18))
    bs=spec['bullet_size']; f=font('p500',sc(bs)); sym=ImageFont.truetype(SYM,sc(bs*0.8)); ind=sc(40)
    maxw=max(d.textlength(b,font=f) for b in spec['bullets'])+ind; x0=cx-maxw/2
    for b in spec['bullets']:
        bb=f.getbbox('H'); sb=sym.getbbox(SPARK)
        d.text((x0,y+bb[1]+((bb[3]-bb[1])-(sb[3]-sb[1]))/2-sb[1]),SPARK,font=sym,fill=CORAL); d.text((x0+ind,y),b,font=f,fill=CREAM)
        y+=sc(bs+12)
    y+=sc(spec.get('gap3',8))
    y+=pill(d,cx,y,pillt,font('p600',sc(spec.get('pill_txt',32))),CORAL,CREAM,sc(28),sc(spec.get('pill_h',60)))
    if tag: y+=sc(10); y+=pill(d,cx,y,tag,font('p600',sc(21)),LIME,DARKTXT,sc(18),sc(38))
    y+=sc(12)
    y+=pill(d,cx,y,button,font('p600',sc(spec.get('pill_txt',32))),LIME,DARKTXT,sc(30),sc(spec.get('pill_h',60)))
    y+=sc(14)
    text_center(d,cx,y,footer,font('p500',sc(22)),CREAM)
    return y+sc(22)

def compose(W,H,scale,art_x,art_y,spec,pillt,tag,button,footer,boutiq,text_y=None):
    art=upscaled(scale); src=np.asarray(art).copy()
    canvas=np.zeros((H,W,3),dtype='uint8')
    need=np.ones((H,W),dtype=bool)               # everything outside the artwork needs grain
    ax0,ay0=art_x,art_y; ax1,ay1=art_x+art.width,art_y+art.height
    cx0,cy0=max(ax0,0),max(ay0,0); cx1,cy1=min(ax1,W),min(ay1,H)
    canvas[cy0:cy1,cx0:cx1]=src[cy0-ay0:cy1-ay0,cx0-ax0:cx1-ax0]; need[cy0:cy1,cx0:cx1]=False
    em=erase_mask(art,scale)                     # old text inside the artwork
    need[cy0:cy1,cx0:cx1]|=em[cy0-ay0:cy1-ay0,cx0-ax0:cx1-ax0]
    # band lookup must be in source coordinates: shift by art_y (band_fill clamps)
    canvas=band_fill(canvas,src,need)
    canvas=Image.fromarray(canvas)
    if boutiq:
        ribbon(canvas,(art_x+int(1060*scale),art_y+int(1478*scale)),'Win een date voor 2 bij BoutiQ Almere',font('p600',int(23*scale)),int(500*scale),int(46*scale))
    d=ImageDraw.Draw(canvas)
    y=text_y if text_y is not None else art_y+int(1548*scale)
    yend=text_block(d,W//2,y,scale,spec,pillt,tag,button,footer)
    return canvas, yend

spec_A={'date':'ZATERDAG 7 NOVEMBER','sub':'19:00 – 22:00 · inloop 18:30',
 'chips':['Singles 25 t/m 40 jaar','Nooit gepadeld? Geen probleem'],
 'bullets':['4 rondes, elke ronde een nieuwe partner','Daarna het laatste uur samen in de bar'],
 'date_size':54,'sub_size':30,'chip_size':24,'chip_h':44,'bullet_size':32,'pill_txt':32,'pill_h':60,'gap1':16,'gap2':18,'gap3':8}
spec_B=dict(spec_A); spec_B.update({'sub':'19:00 – 22:00 · inloop 18:30','date_size':50,'sub_size':28,'chip_size':22,'bullet_size':29,'pill_txt':30,'pill_h':56})

spec_F=dict(spec_B); spec_F.update({'date_size':44,'sub_size':25,'chip_size':20,'chip_h':38,'bullet_size':26,'pill_txt':27,'pill_h':50,'gap1':10,'gap2':12,'gap3':4})

if __name__=='__main__':
    # Poster 3:4 (the artwork's own ratio, no extension, no seam): 2986 x 4000
    S=2.0; W,H=int(OW*S),int(OH*S)
    for name,bq in (('poster-A-print-boutiq',True),('poster-A-print-zonder-boutiq',False)):
        img,yend=compose(W,H,S,0,0,spec_A,'€49,50 p.p. incl. welkomstdrankje & hapjes',None,'Meld je aan → allcourtacademy.com/events','All Court Academy × Poort Padel · Neonweg 62, Almere',bq)
        img.save(f'{name}.png'); print(name,img.size,'text ends at',yend,'of',H)
    # Feed 4:5: scale by height, side margins filled with grain
    W,H=2160,2700; S=H/OH; aw=int(OW*S); ax=(W-aw)//2
    img,yend=compose(W,H,S,ax,0,spec_F,'€49,50 p.p. incl. welkomstdrankje & hapjes',None,'Meld je aan → allcourtacademy.com/events','All Court Academy × Poort Padel · Almere',True)
    img.save('ig-feed-4x5.png'); print('feed',img.size,yend)
    # Story 9:16: scale by width, top/bottom filled with grain, text inside the safe zone
    W,H=2160,3840; S=W/OW; ah=int(OH*S); ay=(H-ah)//2
    img,yend=compose(W,H,S,0,ay,spec_B,'€49,50 p.p. incl. welkomstdrankje & hapjes',None,'Meld je aan → link in bio','All Court Academy × Poort Padel',True)
    img.save('ig-story-9x16.png'); print('story',img.size,yend,'safe until',int(H*0.88))
