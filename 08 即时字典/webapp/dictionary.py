import justpy as jp
from .definition import Definition


class Dictionary:
    path = "/dictionary"

    @classmethod
    def server(cls, request):
        wp = jp.QuasarPage(tailwind=True)
        container = jp.Div(classes="w-1/2", a=wp)
        jp.Div(text="Dictionary", classes="text-6xl font-bold", a=container)

        input_div = jp.Div(classes="grid grid-cols-2 gap-4 ", a=container)
        target_div = jp.Input(
            placeholder="please enter a dictionary",
            classes="m-2 px-2 py-4 border-2 border-blue-200 mt-10 focus:border-blue-600 focus:outline-none",
            a=input_div,
        )

        result_div = jp.Div(classes="mt-10 w-full h-40 border-2", a=container)
        jp.Button(
            text="查询",
            classes="border-2 text-gray-500",
            a=input_div,
            click=cls.get_word,
            result=result_div,
            target=target_div,
        )
        return wp

    @staticmethod
    def get_word(widget, msg):
        word = widget.target.value
        data = Definition(word).get()
        print(Definition(word))
        widget.result.text = data
