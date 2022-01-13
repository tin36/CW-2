import json



def count_views(pk):

    with open('data/data.json', 'r+', encoding='utf-8') as f:
        posts = json.load(f)
        f.seek(0)


        for i in posts:
            if i['pk'] == pk:
                print(i)
            if i['pk'] == pk:
                i['views_count'] += 1
        json.dump(posts, f, indent=2, ensure_ascii=False)


print(count_views(1))