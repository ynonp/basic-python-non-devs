import subprocess

# subprocess.run(["curl",
#                 "--output",
#                 "myfile.tar.gz",
#                 "https://curl.haxx.se/download/curl-7.74.0.tar.gz"
#                 ])

# Read output of command
# import json
# result = subprocess.check_output(['curl', 'http://api.open-notify.org/iss-now.json'])
# data = json.loads(result)
# print(data['message'])


# Run multiple porgrams in parallel
image_urls = [
    'https://images.squarespace-cdn.com/content/v1/5a3adeb11f318d9dd2dfadaa/1527611880550-6DUOWKQ67ULOTK1ODMLQ/ke17ZwdGBToddI8pDm48kFVfgRqeiJbezCllpJQtY_0UqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8N_N4V1vUb5AoIIIbLZhVYxCRW4BPu10St3TBAUQYVKciN1LM1HpqVwNixpz1hCKq8qoxvRXzjNTQ09MieJKwtnXQQXYw_DH5ZQqvplaE488/puppies.jpg?format=1500w',
    'http://cdn.akc.org/content/article-body-image/siberian_husky_cute_puppies.jpg',
    'https://scontent.ftlv2-1.fna.fbcdn.net/v/t1.0-9/125828095_2904258203179278_6699180443166062470_n.jpg?_nc_cat=111&ccb=2&_nc_sid=730e14&_nc_ohc=3XbPNN4VHtsAX8-6gWZ&_nc_ht=scontent.ftlv2-1.fna&oh=794f8f6e044a1fa3d2b8cf594f3df4fb&oe=601BBD3B',
    'https://blog.malwarebytes.com/wp-content/uploads/2017/11/paulie2-599x960-374x600.jpg',
    'http://cdn.akc.org/content/article-body-image/chocolate_lab_cute_puppies.jpg'
]

for index, url in enumerate(image_urls):
    proc = subprocess.run([
        'curl',
        '-s',
        '--output',
        f'file_{index}.jpg',
        url,
    ])







