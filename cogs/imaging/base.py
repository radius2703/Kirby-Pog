from io import BytesIO
from wand.image import Image


def image_edit(image: bytes, edit, **options) -> BytesIO:
    image_final = BytesIO()

    with Image(blob=image) as edit_image:
        with Image(edit_image.sequence[0]) as final:
            final = edit(final, **options)
            final.save(image_final)
    image_final.seek(0)

    return image_final


# Blurs
def blur(image: Image, radius: float, sigma: float) -> Image:
    image.blur(radius=radius, sigma=sigma)
    return image


def gaussian_blur(image: Image, sigma: float) -> Image:
    image.blur(sigma=sigma)
    return image


def motion_blur(image: Image, radius: float, sigma: float, angle: float) -> Image:
    image.motion_blur(radius=radius, sigma=sigma, angle=angle)
    return image


def rotational_blur(image: Image, angle: float) -> Image:
    image.rotational_blur(angle=min(abs(angle), 360))
    return image


# Noise
def despeckle(image: Image) -> Image:
    image.despeckle()
    return image


def kuwahara(image: Image, radius: float, sigma: float) -> Image:
    image.kuwahara(radius=radius, sigma=sigma)
    return image


def spread(image: Image, radius: float) -> Image:
    image.spread(radius=radius)
    return image


def noise(image: Image, noise_type: str, attenuate: float):
    if noise_type not in ("uniform", "random", "poisson", "multiplicative_gaussian", "laplacian", "gaussian",
                          "impulse"):
        noise_type = "poisson"

    image.noise(noise_type, attenuate=attenuate)
    return image


# Emboss, shade
def edge(image: Image, radius: float) -> Image:
    image.edge(radius=radius)
    return image


def emboss(image: Image, radius: float, sigma: float) -> Image:
    image.emboss(radius=radius, sigma=sigma)
    return image


def shade(image: Image, azimuth: float, altitude: float) -> Image:
    image.shade(gray=True, azimuth=azimuth, elevation=altitude)
    return image


# Sharpen
def sharpen(image: Image, radius: float, sigma: float) -> Image:
    image.sharpen(radius=radius, sigma=sigma)
    return image
