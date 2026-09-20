"""Padel & Quiz poster: chalkboard artwork (Higgsfield) + deterministic chalk text block + logos.
Artwork: v1_full.png (1744 x 2336, 3:4). Fonts: Poppins 500/600/700 (font_1/2/3), DejaVuSans-Bold for glyphs.
Outputs: poster 3:4 (print), feed 4:5, story 9:16."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = '/tmp/claude-0/-home-user-Event-cliniqs-poort-Padel/f83b7c81-36ad-57f5-9da0-b9e3c9fcfcb0/scratchpad'
FONTS = {'p500': HERE + '/poster/font_1.ttf', 'p600': HERE + '/poster/font_2.ttf', 'p700': HERE + '/poster/font_3.ttf',
         'dv': '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'}
WHITE = (240, 238, 230)
YELLOW = (242, 204, 92)
DARK = (18, 16, 14)
WALL = (14, 12, 10)
rng = np.random.default_rng(7)


def font(k, s):
    return ImageFont.truetype(FONTS[k], int(s))


def chalk(layer, strength=0.28, blur=0.6):
    """Multiply the alpha of an RGBA layer with chalk-like noise so text looks hand-drawn with chalk."""
    a = np.asarray(layer.split()[3]).astype(np.float32) / 255.0
    n = rng.random(a.shape).astype(np.float32)
    n = np.asarray(Image.fromarray((n * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(blur))).astype(np.float32) / 255.0
    a = a * (1 - strength + strength * n)
    r, g, b, _ = layer.split()
    return Image.merge('RGBA', (r, g, b, Image.fromarray((a * 255).astype(np.uint8))))


def parts(text):
    """Split text so → and ✦ use DejaVu (Poppins has no glyph)."""
    out, buf = [], ''
    for ch in text:
        if ch in '→✦×':
            if buf:
                out.append(('p', buf)); buf = ''
            out.append(('dv', ch))
        else:
            buf += ch
    if buf:
        out.append(('p', buf))
    return out


def text_w(d, text, fk, size):
    w = 0
    for k, s in parts(text):
        f = font(fk if k == 'p' else 'dv', size if k == 'p' else size * 0.9)
        w += d.textlength(s, font=f)
    return w


def draw_text(d, x, y, text, fk, size, fill):
    for k, s in parts(text):
        f = font(fk if k == 'p' else 'dv', size if k == 'p' else size * 0.9)
        dy = 0 if k == 'p' else size * 0.06
        d.text((x, y + dy), s, font=f, fill=fill)
        x += d.textlength(s, font=f)
    return x


def text_center(d, cx, y, text, fk, size, fill):
    w = text_w(d, text, fk, size)
    draw_text(d, cx - w / 2, y, text, fk, size, fill)
    return size * 1.25


def compose(board, cx, y0, S, spec, logos):
    """Draw the chalk text block on `board` (RGBA) starting at y0, centered on cx. Returns end y."""
    W, H = board.size
    layer = Image.new('RGBA', board.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    y = y0
    # 1 date (yellow chalk) with a soft white under-stroke for a chalk double line
    y += text_center(d, cx, y, spec['date'], 'p700', spec['date_size'] * S, YELLOW) + spec['gap'] * S
    # 2 time line
    y += text_center(d, cx, y, spec['sub'], 'p600', spec['sub_size'] * S, WHITE) + spec['gap'] * S
    # 3 chips (outlined chalk)
    cs, ch, pad, gapc = spec['chip_size'] * S, spec['chip_h'] * S, 22 * S, 16 * S
    widths = [text_w(d, c, 'p600', cs) + 2 * pad for c in spec['chips']]
    x = cx - (sum(widths) + gapc * (len(widths) - 1)) / 2
    for c, w in zip(spec['chips'], widths):
        d.rounded_rectangle((x, y, x + w, y + ch), radius=ch / 2, outline=WHITE, width=max(2, int(3 * S)))
        draw_text(d, x + pad, y + (ch - cs * 1.2) / 2, c, 'p600', cs, WHITE)
        x += w + gapc
    y += ch + spec['gap'] * S * 1.3
    # 4 bullets, left aligned as a block
    bs = spec['bullet_size'] * S
    bw = max(text_w(d, b, 'p500', bs) for b in spec['bullets']) + 46 * S
    bx = cx - bw / 2
    for b in spec['bullets']:
        draw_text(d, bx, y + bs * 0.08, '✦', 'p500', bs * 0.85, YELLOW)
        draw_text(d, bx + 46 * S, y, b, 'p500', bs, WHITE)
        y += bs * 1.35
    y += spec['gap'] * S * 0.8
    # 5 price pill (yellow chalk fill, dark text)
    ps, ph = spec['pill_txt'] * S, spec['pill_h'] * S
    pw = text_w(d, spec['pill'], 'p700', ps) + 60 * S
    d.rounded_rectangle((cx - pw / 2, y, cx + pw / 2, y + ph), radius=ph / 2, fill=YELLOW)
    draw_text(d, cx - pw / 2 + 30 * S, y + (ph - ps * 1.2) / 2, spec['pill'], 'p700', ps, DARK)
    y += ph + spec['gap'] * S
    # 6 button (white chalk fill)
    bts, bth = spec['btn_txt'] * S, spec['btn_h'] * S
    btw = text_w(d, spec['btn'], 'p700', bts) + 60 * S
    d.rounded_rectangle((cx - btw / 2, y, cx + btw / 2, y + bth), radius=bth / 2, fill=WHITE)
    draw_text(d, cx - btw / 2 + 30 * S, y + (bth - bts * 1.2) / 2, spec['btn'], 'p700', bts, DARK)
    y += bth + spec['gap'] * S * 1.4
    layer = chalk(layer, 0.30, 0.7)
    board.alpha_composite(layer)
    # 7 logos row (crisp, not chalked): ACA × Poort Padel
    lh = spec['logo_h'] * S
    aca = logos['aca'].copy(); aca.thumbnail((10000, lh))
    pp = logos['pp'].copy(); pp.thumbnail((10000, lh * 0.82))
    xf = font('dv', 30 * S)
    gap = 34 * S
    total = aca.width + gap + 30 * S + gap + pp.width
    x = cx - total / 2
    board.alpha_composite(aca, (int(x), int(y + (lh - aca.height) / 2)))
    x += aca.width + gap
    ImageDraw.Draw(board).text((x, y + lh / 2 - 22 * S), '×', font=xf, fill=WHITE)
    x += 30 * S + gap
    board.alpha_composite(pp, (int(x), int(y + (lh - pp.height) / 2)))
    y += lh + 10 * S
    # 8 address
    l2 = Image.new('RGBA', board.size, (0, 0, 0, 0))
    text_center(ImageDraw.Draw(l2), cx, y, spec['addr'], 'p500', spec['addr_size'] * S, WHITE)
    board.alpha_composite(chalk(l2, 0.25, 0.6))
    y += spec['addr_size'] * S * 1.3
    return y


SPEC = {
    'date': 'ZATERDAG 16 JANUARI', 'date_size': 74,
    'sub': '18:00 – 22:00 · inloop 17:30', 'sub_size': 38,
    'chips': ['Alleen of met je team', 'Alle niveaus, rackets liggen klaar'], 'chip_size': 27, 'chip_h': 52,
    'bullets': ['1,5 uur Mexicano, daarna pubquiz in teams van 4', '€500 aan prijzen van Poort Padel'], 'bullet_size': 34,
    'pill': '€39,50 p.p. incl. welkomstdrankje & hapjes', 'pill_txt': 36, 'pill_h': 64,
    'btn': 'Meld je aan → allcourtacademy.com/events', 'btn_txt': 33, 'btn_h': 60,
    'logo_h': 74, 'addr': 'Poort Padel · Neonweg 62, Almere', 'addr_size': 22, 'gap': 11,
}


def load_logos(aca_file):
    return {'aca': Image.open(HERE + '/quiz/' + aca_file).convert('RGBA'),
            'pp': Image.open(HERE + '/quiz/logo_pp_white.png').convert('RGBA')}


def poster(art, logos, y0=1665, S=2.0):
    """Upscale the artwork S x (Lanczos + unsharp, same as the dating poster) and draw the text at scale S."""
    src = Image.open(art).convert('RGB')
    big = src.resize((int(src.width * S), int(src.height * S)), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.5, 60, 2))
    board = big.convert('RGBA')
    yend = compose(board, board.width / 2, y0 * S, S, SPEC, logos)
    return board, yend


if __name__ == '__main__':
    import sys
    aca_file = sys.argv[1] if len(sys.argv) > 1 else 'logo_aca_site.png'
    tag = sys.argv[2] if len(sys.argv) > 2 else 'site'
    logos = load_logos(aca_file)
    # Poster 3:4 at 2x (3488 x 4672 = 295 dpi at 30 x 40 cm)
    board, yend = poster(HERE + '/quiz/v1_full.png', logos)
    print('poster', board.size, 'text ends at', yend)
    rgb = board.convert('RGB')
    rgb.save(HERE + f'/quiz/quiz-poster-{tag}.jpg', quality=95)
    rgb.save(HERE + f'/quiz/quiz-poster-{tag}-30x40cm.pdf', resolution=board.width / (30 / 2.54))
    # Feed 4:5 (2160 x 2700): board fitted by height, dark wall left/right
    fb = rgb.resize((int(board.width * 2700 / board.height), 2700), Image.LANCZOS)
    feed = Image.new('RGB', (2160, 2700), WALL); feed.paste(fb, ((2160 - fb.width) // 2, 0))
    feed.save(HERE + f'/quiz/quiz-feed-{tag}.jpg', quality=95)
    # Story 9:16 (2160 x 3840): board fitted by width, dark wall top/bottom
    sb = rgb.resize((2160, int(board.height * 2160 / board.width)), Image.LANCZOS)
    story = Image.new('RGB', (2160, 3840), WALL); story.paste(sb, (0, (3840 - sb.height) // 2))
    story.save(HERE + f'/quiz/quiz-story-{tag}.jpg', quality=95)
    print('feed', feed.size, 'story', story.size)
