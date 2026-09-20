import random, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
random.seed(7)
SRC='../../images/11.webp'
orig=Image.open(SRC).convert('RGB')          # 1493 x 2000
OW,OH=orig.size
CREAM=(233,212,175); CORAL=(224,64,40); LIME=(194,193,0); DARK=(5,39,25); DARKTXT=(4,28,18)
F={'p500':'font_1.ttf','p600':'font_2.ttf','p700':'font_3.ttf'}
def font(k,s): return ImageFont.truetype(F[k],s)
SYM='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def rich_parts(txt,fnt):
    """split text so that arrows/sparkles are drawn with DejaVu (Poppins lacks them)"""
    sym=ImageFont.truetype(SYM,int(fnt.size*0.9)); parts=[]; buf=''
    for ch in txt:
        if ch in '\u2192\u2726':
            if buf: parts.append((buf,fnt)); buf=''
            parts.append((ch,sym))
        else: buf+=ch
    if buf: parts.append((buf,fnt))
    return parts
def rich_len(d,txt,fnt): return sum(d.textlength(t,font=f) for t,f in rich_parts(txt,fnt))
def rich_draw(d,x,y,txt,fnt,fill):
    base=fnt.getbbox('Hg')
    for t,f in rich_parts(txt,fnt):
        bb=f.getbbox('Hg'); dy=(base[3]-bb[3])  # align baselines roughly
        d.text((x,y+dy),t,font=f,fill=fill); x+=d.textlength(t,font=f)

# --- texture from clean patches of the original background
def clean_patch(p):
    a=np.asarray(p).astype(int); bg=np.array([5,39,25]); bad=np.abs(a-bg).sum(2)>45
    med=np.median(a[~bad],axis=0)
    noise=np.random.default_rng(3).normal(0,5,a.shape)
    a[bad]=np.clip(med+noise[bad],0,255)
    return Image.fromarray(a.astype('uint8'))
patches=[clean_patch(orig.crop(r)) for r in [(1310,1500,1493,1800),(0,1620,300,1800),(1240,1480,1493,1800)]]
def texture(w,h,scale):
    canvas=Image.new('RGB',(w,h),DARK)
    tiles=[p.resize((int(p.width*scale),int(p.height*scale)),Image.LANCZOS) for p in patches]
    y=0
    while y<h:
        x=0; rowh=None
        while x<w:
            t=random.choice(tiles)
            if random.random()<0.5: t=t.transpose(Image.FLIP_LEFT_RIGHT)
            if random.random()<0.5: t=t.transpose(Image.FLIP_TOP_BOTTOM)
            cw=min(t.width,random.randint(120,260)); ch=min(t.height,random.randint(120,260))
            ox=random.randint(0,t.width-cw); oy=random.randint(0,t.height-ch)
            c=t.crop((ox,oy,ox+cw,oy+ch)); canvas.paste(c,(x,y)); x+=cw; rowh=ch if rowh is None else min(rowh,ch)
        y+=rowh
    return canvas

def feather_paste(canvas, img, pos, feather=40):
    """paste img with soft edges so the join with the texture is invisible"""
    m=Image.new('L',img.size,255); d=ImageDraw.Draw(m)
    d.rectangle((0,0,img.width-1,img.height-1),outline=0,width=feather)
    m=m.filter(ImageFilter.GaussianBlur(feather/2))
    canvas.paste(img,pos,m)

def artwork(scale, cut=1540):
    """upscaled original down to y=cut (below the polaroid), with the side doodles kept to y=1600"""
    a=orig.resize((int(OW*scale),int(OH*scale)),Image.LANCZOS)
    a=a.filter(ImageFilter.UnsharpMask(radius=1.5,percent=60,threshold=2))
    return a, int(cut*scale)

def text_center(d,cx,y,txt,fnt,fill):
    w=rich_len(d,txt,fnt); rich_draw(d,cx-w/2,y,txt,fnt,fill); return fnt.size

def pill(d,cx,y,txt,fnt,bg,fg,padx,h,radius=None):
    w=rich_len(d,txt,fnt)+2*padx; r=radius or h//2
    d.rounded_rectangle((cx-w/2,y,cx+w/2,y+h),radius=r,fill=bg)
    bbox=fnt.getbbox('Hg'); th=bbox[3]-bbox[1]
    rich_draw(d,cx-(w-2*padx)/2,y+(h-th)/2-bbox[1],txt,fnt,fg)
    return h

def ribbon(canvas,center,txt,fnt,w,h,angle=-9):
    layer=Image.new('RGBA',(w+80,h+80),(0,0,0,0)); d=ImageDraw.Draw(layer)
    d.rounded_rectangle((40,40,40+w,40+h),radius=18,fill=CORAL+(255,))
    tw=d.textlength(txt,font=fnt); bb=fnt.getbbox(txt)
    d.text((40+(w-tw)/2,40+(h-(bb[3]-bb[1]))/2-bb[1]),txt,font=fnt,fill=CREAM)
    layer=layer.rotate(angle,resample=Image.BICUBIC,expand=True)
    canvas.paste(layer,(int(center[0]-layer.width/2),int(center[1]-layer.height/2)),layer)

SPARK='\u2726'
def compose(W,H,scale,art_x,art_y,cut,spec,pillt,tag,button,footer,boutiq,top_free=0):
    canvas=texture(W,H,scale)
    a,cuty=artwork(scale,cut)
    # hard paste of the artwork (no feathering: the join sits on plain background under the polaroid)
    canvas.paste(a.crop((0,0,a.width,cuty)),(art_x,art_y))
    # keep the side doodles a little lower than the cut (left sparkle sits at y 1540-1600 in the original)
    s=int(300*scale); extra=int(60*scale)
    canvas.paste(a.crop((0,cuty,s,cuty+extra)),(art_x,art_y+cuty))
    canvas.paste(a.crop((a.width-s,cuty,a.width,cuty+extra)),(art_x+a.width-s,art_y+cuty))
    # soften only the texture side of the seams (dark on dark), never the artwork
    seam=Image.new('L',(W,H),0); sd=ImageDraw.Draw(seam)
    f=int(6*scale)
    sd.rectangle((art_x+s-f,art_y+cuty,art_x+a.width-s+f,art_y+cuty+extra+f),fill=255)
    sd.rectangle((art_x-f,art_y+cuty+extra,art_x+a.width+f,art_y+cuty+extra+2*f),fill=255)
    seam=seam.filter(ImageFilter.GaussianBlur(f))
    blurred=canvas.filter(ImageFilter.GaussianBlur(int(2*scale)))
    canvas.paste(blurred,(0,0),seam)
    if boutiq:
        ribbon(canvas,(art_x+int(1060*scale),art_y+int(1478*scale)),'Win een date voor 2 bij BoutiQ Almere',font('p600',int(23*scale)),int(500*scale),int(46*scale))
    d=ImageDraw.Draw(canvas); cx=W//2
    y=art_y+cuty+int(spec.get('top',22)*scale)
    sc=lambda v:int(v*scale)
    f=font('p700',sc(spec.get('date_size',50))); y+=text_center(d,cx,y,spec['date'],f,CREAM)+sc(6)
    f=font('p600',sc(spec.get('sub_size',29))); y+=text_center(d,cx,y,spec['sub'],f,CORAL)+sc(22)
    f=font('p600',sc(spec.get('chip_size',22))); padx=sc(18); gap=sc(14); h=sc(46)
    widths=[rich_len(d,c,f)+2*padx for c in spec['chips']]; total=sum(widths)+gap*(len(widths)-1)
    x=cx-total/2
    for c,w in zip(spec['chips'],widths):
        d.rounded_rectangle((x,y,x+w,y+h),radius=h//2,fill=CREAM)
        bb=f.getbbox('Hg'); rich_draw(d,x+padx,y+(h-(bb[3]-bb[1]))/2-bb[1],c,f,DARKTXT); x+=w+gap
    y+=h+sc(24)
    bs=spec.get('bullet_size',30)
    f=font('p500',sc(bs)); sym=ImageFont.truetype(SYM,sc(bs*0.8))
    ind=sc(40); maxw=max(d.textlength(b,font=f) for b in spec['bullets'])+ind; x0=cx-maxw/2
    for b in spec['bullets']:
        bb=f.getbbox('H'); sb=sym.getbbox(SPARK)
        d.text((x0,y+bb[1]+((bb[3]-bb[1])-(sb[3]-sb[1]))/2-sb[1]),SPARK,font=sym,fill=CORAL); d.text((x0+ind,y),b,font=f,fill=CREAM)
        y+=sc(bs+14)
    y+=sc(12)
    y+=pill(d,cx,y,pillt,font('p600',sc(33)),CORAL,CREAM,sc(28),sc(64))
    if tag:
        y+=sc(10); y+=pill(d,cx,y,tag,font('p600',sc(22)),LIME,DARKTXT,sc(18),sc(40))
    y+=sc(14)
    y+=pill(d,cx,y,button,font('p600',sc(33)),LIME,DARKTXT,sc(30),sc(64))
    y+=sc(18)
    text_center(d,cx,y,footer,font('p500',sc(24)),CREAM)
    return canvas

# ---------- Poster 2:3 (print) ----------
S=2.0; W=int(OW*S); H=int(W*1.5)
spec_A={'date':'ZATERDAG 7 NOVEMBER','sub':'19:00 \u2013 22:00 \u00b7 inloop 18:30',
 'chips':['Singles 25 t/m 40 jaar','Nooit gepadeld? Geen probleem'],
 'bullets':['4 rondes, elke ronde een nieuwe partner','Daarna het laatste uur samen in de bar'],
 'top':40,'date_size':60,'sub_size':34,'chip_size':26,'bullet_size':35}
for name,bq in (('poster-A-print-boutiq',True),('poster-A-print-zonder-boutiq',False)):
    img=compose(W,H,S,0,0,1540,spec_A,'€49,50 p.p. incl. welkomstdrankje & hapjes',None,'Meld je aan → allcourtacademy.com/events','All Court Academy × Poort Padel · Neonweg 62, Almere',bq)
    img.save(f'{name}.png'); print(name,img.size)

# ---------- Instagram feed 4:5 ----------
W,H=2160,2700; S=1.25; aw=int(OW*S); ax=(W-aw)//2
spec_B={'date':'ZATERDAG 7 NOVEMBER','sub':'19:00 \u2013 22:00',
 'chips':['Singles 25 t/m 40 jaar','Nooit gepadeld? Geen probleem'],
 'bullets':['4 rondes, elke ronde een nieuwe partner','Daarna het laatste uur samen in de bar'],
 'top':18,'date_size':48,'sub_size':29,'chip_size':23,'bullet_size':29}
img=compose(W,H,S,ax,0,1540,spec_B,'€49,50 p.p. incl. welkomstdrankje & hapjes','Match = gratis baanuur','Meld je aan → allcourtacademy.com/events','All Court Academy × Poort Padel · Almere',True)
img.save('ig-feed-4x5.png'); print('feed',img.size)

# ---------- Instagram story 9:16 ----------
W,H=2160,3840; S=1.44; aw=int(OW*S); ax=(W-aw)//2; ay=int(H*0.08)
spec_S=dict(spec_B)
img=compose(W,H,S,ax,ay,1540,spec_S,'€49,50 p.p. incl. welkomstdrankje & hapjes','Match = gratis baanuur','Meld je aan → link in bio','All Court Academy × Poort Padel',True)
img.save('ig-story-9x16.png'); print('story',img.size)
