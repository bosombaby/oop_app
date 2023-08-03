import justpy as jp


@jp.SetRoute("/")
def hello():
    wp = jp.WebPage()
    jp.Div(text="Hello111", a=wp, classes="bg-blue-500")
    return wp


@jp.SetRoute("/home")
def home():
    wp = jp.QuasarPage(tailwind=True)

    container = jp.Div(classes="flex mt-48 space-x-6 w-1/2 mx-auto", a=wp)
    in_1 = jp.Input(
        placeholder="Enter First Value", classes="form-input border-0", a=container
    )
    in_2 = jp.Input(
        placeholder="Enter Second Value", classes="form-input border-0", a=container
    )
    ouput_value = jp.Div(
        text="",
        classes="px-6 py-2 border border-blue-300",
        a=container,
    )
    jp.Button(
        text="计算",
        classes="px-6 py-2 bg-blue-300 hover:bg-blue-700 hover:text-white transition",
        a=container,
        click=cal_sum,
        in1=in_1,
        in2=in_2,
        out=ouput_value,
    )
    return wp


def cal_sum(widget, msg):
    result = float(widget.in1.value) + float(widget.in2.value)
    widget.out.text = result


# jp.Route("/home", home)

jp.justpy()
