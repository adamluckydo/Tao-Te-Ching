from PIL import Image, ImageDraw

def create_icon(size):
    img = Image.new('RGB', (size, size), '#1a1a1a')
    draw = ImageDraw.Draw(img)
    
    # Draw a simple circle (representing wholeness/tao)
    margin = size // 8
    circle_bbox = [margin, margin, size - margin, size - margin]
    draw.ellipse(circle_bbox, outline='#e8e4dc', width=max(2, size // 64))
    
    # Inner smaller circle
    inner_margin = size // 3
    inner_bbox = [inner_margin, inner_margin, size - inner_margin, size - inner_margin]
    draw.ellipse(inner_bbox, outline='#e8e4dc', width=max(1, size // 96))
    
    return img

# Generate icons
create_icon(192).save('icon-192.png')
create_icon(512).save('icon-512.png')
print("Icons created")
