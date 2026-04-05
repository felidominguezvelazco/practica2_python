def analizar_hashtags(posts):
    conteo = {}

    for post in posts:
        palabras = post.split()

        for palabra in palabras:
            if palabra.startswith("#"):
                hashtag = palabra.strip()

                if hashtag in conteo:
                    conteo[hashtag] += 1
                else:
                    conteo[hashtag] = 1

    trending = {k: v for k, v in conteo.items() if v > 1}

    return conteo, trending