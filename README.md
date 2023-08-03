# 一、前言
Python OOP 编程指的是使用面向对象编程（Object-Oriented Programming，简称 OOP）的方式来编写 Python 代码。面向对象编程是一种编程范式，它将数据和操作数据的方法组合成一个对象，通过对象之间的交互来实现程序的功能。
在 Python 中，可以使用类（class）来定义对象的属性和方法。类是一种自定义的数据类型，它可以包含多个属性和方法，用于描述某个对象的特征和行为。通过创建类的实例（instance），可以在程序中使用该类定义的对象。
面向对象编程的主要思想是将程序中的数据和操作数据的方法封装在一个对象中，从而实现数据的抽象和封装。这样可以使程序更加模块化、可维护和可扩展，同时也可以提高代码的复用性和可读性。
Python OOP 编程中常用的一些概念包括：

- 类（class）：用于定义对象的属性和方法的模板。
- 对象（object）：类的实例，包含了类定义的属性和方法。
- 属性（attribute）：对象的数据成员，用于描述对象的特征。
- 方法（method）：对象的函数成员，用于描述对象的行为。
- 继承（inheritance）：一种机制，用于创建新的类并从现有类中继承属性和方法。
- 多态（polymorphism）：一种机制，允许不同的对象对同一消息做出不同的响应。

需要注意的是，虽然 Python 支持面向对象编程，但并不是所有的 Python 代码都需要使用面向对象编程的方式来实现。在实际编程中，应该根据具体的需求和场景来选择合适的编程范式。

[Just a moment...](https://www.udemy.com/course/the-python-pro-course/)
# 二、账单应用

![18.png](https://cdn.nlark.com/yuque/0/2023/png/27367619/1690937053413-ba3651e6-97b4-4437-b806-e54de8bf41ac.png#averageHue=%23fbfaf9&clientId=ufb0db16a-672b-4&from=ui&id=u789fae46&originHeight=674&originWidth=1097&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=24955&status=done&style=none&taskId=u7c717280-06f3-4a19-965b-30c2dd9b9ab&title=)
分为室友、账单、PDF报告三个类，彼此相互联系。
# 三、绘图应用

![1.png](https://cdn.nlark.com/yuque/0/2023/png/27367619/1690937134175-e7b15e7c-fd3c-47b4-8447-c3a2cd4e9450.png#averageHue=%23ffff00&clientId=ufb0db16a-672b-4&from=ui&id=u589bdb53&originHeight=804&originWidth=894&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=5747&status=done&style=none&taskId=u8e668682-a232-4a34-8196-6cf65cc4caf&title=)

绘图应用分为画布、长方形、正方形类。通过Image.fromarray可以把3维数组里面的rgb值转为像素点图像。
# 四、图片搜索
[Welcome to Kivy — Kivy 2.2.1 documentation](https://kivy.org/doc/stable/)

Kivy 是一个用于创建跨平台用户界面（User Interface，简称 UI）的 Python 框架。它可以让开发者使用 Python 语言来创建具有丰富交互性和视觉效果的应用程序，支持多点触控、手势识别、动画效果等高级功能。
Kivy 的主要特点包括：

- 跨平台：Kivy 可以在多个平台上运行，包括 Windows、macOS、Linux、Android、iOS 等。
- 开源：Kivy 是一个开源框架，可以免费使用和修改。
- Pythonic：Kivy 的 API 设计符合 Python 的风格和习惯，易于学习和使用。
- 响应式布局：Kivy 使用一种称为 Kv 语言的声明式语言来定义用户界面，支持自适应布局和响应式设计。
- 多点触控：Kivy 支持多点触控和手势识别，可以创建具有丰富交互性的应用程序。
- 动画效果：Kivy 支持多种动画效果，可以创建具有流畅动画的应用程序。
- 扩展性：Kivy 可以通过插件和扩展来扩展其功能，例如支持各种输入设备、音频和视频处理等。

Kivy 的应用场景包括游戏开发、移动应用程序开发、嵌入式系统开发等。如果你想使用 Python 来创建具有丰富交互性和视觉效果的应用程序，Kivy 是一个不错的选择。

![2.png](https://cdn.nlark.com/yuque/0/2023/png/27367619/1690937394618-2ee639fd-5745-48be-8521-7a53502efcad.png#averageHue=%237fb7cc&clientId=ufb0db16a-672b-4&from=ui&id=uc617e89a&originHeight=774&originWidth=984&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=855633&status=done&style=none&taskId=uc22e5d3d-cfce-4818-9da3-353c4ffc9d7&title=)

.kv文件就相当于前端的布局样式组件，注意要和主程序放在同一级目录下面。
# 四、摄像头
[The Best File Uploader & Upload API - Filestack](https://www.filestack.com/)

Filestack 是一个云文件处理服务，它可以让开发者轻松地将文件上传到云端，并进行各种文件处理操作，例如转换、裁剪、压缩、水印等。Filestack 支持多种文件类型和云存储服务，包括 Amazon S3、Google Cloud Storage、Azure Blob Storage 等。

本应用分为三个类：相机拍摄、截图生成，生成在线图片链接

# 六、卡路里计算器
[timeanddate.com](https://www.timeanddate.com/)

一个温度类、卡路里类，温度通过上面网站的html进行爬取操作（简单爬虫）。

# 七、邮件自动化
```
# 中国国内现在注册不了google，无法通过代码接入google
# https://learnku.com/python/t/47406
```
[一次性电子邮件服务](https://dropmail.me/zh/)

只需要一个新闻类就可以
# 八、即时字典
[JustPy](https://justpy.io/)


JustPy 是一个用于构建 Web 应用程序的 Python 框架，它使用 Python 语言和 JavaScript 库来创建动态 Web 页面。JustPy 的设计目标是使 Web 开发变得简单、快速和有趣，同时提供强大的功能和灵活性。
JustPy 的主要特点包括：

- 简单易用：JustPy 的 API 设计简单易用，使得开发者可以快速上手并构建出高质量的 Web 应用程序。
- 高性能：JustPy 使用异步编程模型和 WebSockets 技术，可以实现高性能的 Web 应用程序。
- 交互性：JustPy 支持实时数据更新和交互式用户界面，可以创建具有丰富交互性的 Web 应用程序。
- 可扩展性：JustPy 支持使用 Python 和 JavaScript 库来扩展其功能，可以满足各种不同的需求。

JustPy 的工作原理是将 Python 代码转换为 JavaScript 代码，并在浏览器中执行。这样，开发者可以使用 Python 语言来编写 Web 应用程序，而无需学习 JavaScript 语言。同时，JustPy 还提供了一些内置的 JavaScript 库，可以方便地实现各种常见的 Web 功能，例如图表、表单、地图等。
总之，JustPy 是一个强大而易用的 Python Web 框架，可以帮助开发者快速构建出高质量的 Web 应用程序。

**JustPy 自带 Tailwind CSS。在 JustPy 中，可以使用 Tailwind CSS 来快速创建美观的 Web 页面。JustPy 将 Tailwind CSS 集成到其框架中，使得可以直接在 Python 代码中使用 Tailwind CSS 类来设置样式。**

![3.png](https://cdn.nlark.com/yuque/0/2023/png/27367619/1691029706910-fe739717-9fd0-4a7c-ba14-c72ebdebbc36.png#averageHue=%2309101c&clientId=u2d834a4f-2b74-4&from=ui&id=u1ac51cde&originHeight=868&originWidth=1897&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=99563&status=done&style=none&taskId=uaf15cbf0-e97b-4894-a649-77051cd3254&title=)

[Quasar ](https://quasar.dev/)是一个基于 Vue.js 的开源 UI 组件库和工具集，旨在帮助开发人员快速构建高质量的 Web 应用程序和移动应用程序。Quasar 提供了大量的 UI 组件和工具，包括布局、表单、导航、对话框、通知、图标、动画等，可以帮助开发人员快速构建美观、响应式的用户界面。
Quasar 还提供了一些有用的工具，如 CLI 工具、打包工具、代码生成器等，可以帮助开发人员更轻松地管理和构建应用程序。Quasar 还支持多种构建目标，包括 Web 应用程序、移动应用程序、桌面应用程序等，可以满足不同平台和设备的需求。
Quasar 的特点包括：

- 多种构建目标：支持 Web 应用程序、移动应用程序、桌面应用程序等多种构建目标。
- 多种主题：提供多种主题和颜色方案，可以轻松定制应用程序的外观。
- 多语言支持：支持多种语言和国际化，可以轻松创建多语言应用程序。
- 大量组件和工具：提供大量的 UI 组件和工具，可以帮助开发人员快速构建应用程序。
- 简单易用：使用简单、易于学习的 API，可以快速上手并提高开发效率。

总之，Quasar 是一个基于 Vue.js 的开源 UI 组件库和工具集，提供了大量的 UI 组件和工具，可以帮助开发人员快速构建高质量的 Web 应用程序和移动应用程序。





