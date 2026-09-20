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

def compose(W,H,scale,art_x,art_y,cut,lines,pillt,tag,button,footer,boutiq,top_free=0):
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
    y=art_y+cuty+int(18*scale)
    for txt,key,size,col,gap in lines:
        fnt=font(key,int(size*scale)); text_center(d,cx,y,txt,fnt,col); y+=int((size+gap)*scale)
    y+=int(8*scale)
    y+=pill(d,cx,y,pillt,font('p600',int(33*scale)),CORAL,CREAM,int(28*scale),int(64*scale))
    if tag:
        y+=int(10*scale); y+=pill(d,cx,y,tag,font('p600',int(22*scale)),LIME,DARKTXT,int(18*scale),int(40*scale))
    y+=int(14*scale)
    y+=pill(d,cx,y,button,font('p600',int(33*scale)),LIME,DARKTXT,int(30*scale),int(64*scale))
    y+=int(18*scale)
    text_center(d,cx,y,footer,font('p500',int(24*scale)),CREAM)
    return canvas

# ---------- Poster 2:3 (print) ----------
S=2.0; W=int(OW*S); H=int(W*1.5)
lines_A=[
 ('Speel. Praat. Match.','p700',44,CREAM,14),
 ('Zaterdag 7 november · 19:00 – 22:00 · inloop 18:30','p600',35,CREAM,12),
 ('Singles van 25 t/m 40 jaar · 12 dames & 12 heren','p600',31,CREAM,10),
 ('4 rondes, elke ronde een nieuwe partner','p500',30,CREAM,6),
 ('12 min spelen, 12 min praten','p500',30,CREAM,6),
 ('Daarna: het laatste uur samen in de bar','p500',30,CREAM,12),
 ('✦ Nooit gepadeld? Geen probleem, rackets liggen klaar','p500',25,LIME,14),
]
for name,bq in (('poster-A-print-boutiq',True),('poster-A-print-zonder-boutiq',False)):
    img=compose(W,H,S,0,0,1540,lines_A,'€49,50 p.p. incl. welkomstdrankje & hapjes',None,'Meld je aan → allcourtacademy.com/events','All Court Academy × Poort Padel · Neonweg 62, Almere',bq)
    img.save(f'{name}.png'); print(name,img.size)

# ---------- Instagram feed 4:5 ----------
W,H=2160,2700; S=1.25; aw=int(OW*S); ax=(W-aw)//2
lines_B=[
 ('Zaterdag 7 november · 19:00','p700',38,CREAM,12),
 ('Singles 25 t/m 40 jaar · 12 dames & 12 heren','p600',30,CREAM,8),
 ('4 rondes, elke ronde een nieuwe partner','p500',29,CREAM,6),
 ('Daarna samen in de bar · Nooit gepadeld? Geen probleem','p500',26,CREAM,10),
]
img=compose(W,H,S,ax,0,1540,lines_B,'€49,50 p.p. incl. welkomstdrankje & hapjes','Match = gratis baanuur','Meld je aan → allcourtacademy.com/events','All Court Academy × Poort Padel · Almere',True)
img.save('ig-feed-4x5.png'); print('feed',img.size)

# ---------- Instagram story 9:16 ----------
W,H=2160,3840; S=1.44; aw=int(OW*S); ax=(W-aw)//2; ay=int(H*0.08)
lines_S=[
 ('Zaterdag 7 november · 19:00 – 22:00','p700',38,CREAM,12),
 ('Singles 25 t/m 40 jaar · 12 dames & 12 heren','p600',30,CREAM,8),
 ('4 rondes, elke ronde een nieuwe partner','p500',29,CREAM,6),
 ('Daarna samen in de bar · Nooit gepadeld? Geen probleem','p500',26,CREAM,10),
]
img=compose(W,H,S,ax,ay,1540,lines_S,'€49,50 p.p. incl. welkomstdrankje & hapjes','Match = gratis baanuur','Meld je aan → link in bio','All Court Academy × Poort Padel',True)
img.save('ig-story-9x16.png'); print('story',img.size)
