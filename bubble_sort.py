# coding: utf-8


class BubbleSort:

    @classmethod
    def sort(cls, random_list):
        for index in range(len(random_list)):
            for index in range(len(random_list) - 1):
                prev_item, next_item = random_list[index], random_list[index + 1]
                if prev_item > next_item:
                    random_list.insert(
                        random_list.index(next_item) + 1,
                        random_list.pop(random_list.index(prev_item))
                    )
