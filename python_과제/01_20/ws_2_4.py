information = dict()
authors = ['김시습', '허균', '남영로', '작자 미상', '임제']

books = [
    ['금오신화', '이생규장전', '만복자서포기'],
    ['홍길동전', '장생전', '도문대작'],
    ['옥루몽', '옥련몽'],
    ['장화홍련전', '가락국 신화', '온달 설화'],
    ['수성지', '백호집', '원생몽유록']
]

information = {authors[i]: books[i] for i in range(len(authors))}

for author in information:
    print(author)
    for book in information[author]:
        print(f'  {book}')