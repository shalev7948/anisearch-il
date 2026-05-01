import requests

WEBHOOK = "https://discord.com/api/webhooks/1499062652742402113/mRdakce78ASxWaYr99aEyTqfQ9OBzeTKjk_x2Xe7dkO9pk-XsbM4AKtGv5tlG5VeuAmm"

def send(title, episode, url, image):
    data = {
        "embeds": [
            {
                "title": f"{title} פרק {episode}",
                "url": url,
                "image": {"url": image}
            }
        ]
    }

    requests.post(WEBHOOK, json=data)
