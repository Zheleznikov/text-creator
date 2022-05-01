import markovify


def create_random_text(number_of_sentences):
    text = open('example.txt', encoding='utf8').read()
    text_model = markovify.Text(text)
    for i in range(number_of_sentences):
        print(text_model.make_sentence())


if __name__ == '__main__':
    # как можно сделать
    # 1. выделить в шаблоне места, в которых будет КИ
    # 2. написать функцию, которая будет подставлять соответствующее случайное КИ в нужное место
    # 3. создать новый текст с вымышленным КИ в шаблоне
    # 4. Создать случайный текст с помощью цепей Маркова
    create_random_text(10)
    # 5. Записать это текст в нужный формат
