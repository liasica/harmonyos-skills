---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-next-code-refactoring
title: 代码重构
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码重构
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-11-23
content_hash: sha256:a0598c88288241a5636ef99d4b038f447589856ff262ca714259663725a2d305
---

## ArkTS/TS代码重构

### 安全删除

编辑器支持安全删除功能，帮助开发者安全地删除代码中的标识符对象（变量、函数或类等）或删除指定文件。在删除前，编辑器会先在代码中搜索对该对象的引用，如果存在引用，编辑器将提示开发者进行必要的检查和调整。

**使用方式：**在编辑器内选中需要删除的标识符对象，右键单击**重构**，选择**安全删除**，单击**确认**后将自动检查当前对象在代码中被引用的情况，点击**查看引用**可查看具体使用的代码内容，点击**删除**将直接删除该对象的定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/0riZQx-FS-2GwA4VK6v1gg/zh-cn_image_0000002820721037.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=13BCC3757909E62CB8E831F1872D8499D884FB821C53C6A0587CD07BB006F897)

### 代码重命名

代码编辑支持重命名功能，可以快速更改变量、函数、类、类成员等相关标识符及文件、文件夹的名称，并同步到整个工程中对其进行引用的位置。

**使用方式：**选中需要重新命名的标识符（变量、类、接口、函数等），右键单击**重构 > 重命名**（或快捷键**Shift+F6**），在弹框中输入新的标识符名称，点击**重命名**完成变量重命名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/I38b1B8ARl6-egX_AapyVA/zh-cn_image_0000002820681029.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=B953F66BD3C9A5682E12E4BA30CCB05F2A7AB3191217BB9E2053F8C2AD091C15)

代码重命名支持预览功能。在**重命名**弹窗中点击**预览**，编辑器左侧的预览列表中查看变量被引用的位置。

**说明** 

若ArkTS文件中存在C++接口调用，使用Rename进行重命名时，C++文件中涉及的函数名也会被重命名。

### 代码提取

在编辑器中支持将函数内、类方法内等区域代码块或表达式，提取为新变量（Variable）、方法/函数（Method）、常量（Constant）、接口（Interface）、变量（Variable）或类型别名（Type Alias）。准确便捷地将所选区域代码从当前作用域内进行提取，提升编码效率。选中所需要提取的代码块，右键单击**重构**，选择需要提取的类型。

* 将选中的表达式提取为变量（Variable）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/DUhySMCgRouzQ0En-e2ATg/zh-cn_image_0000002820681037.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=334109838515A278E76A2A91A1D1C889CD9BEE090111AED2C25F7BA85097C4FC)
* 将选中的单行表达式提取为常量（Constant）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/yVQhbv5XRAyKWwpEXp25-A/zh-cn_image_0000002792001068.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=9FE76A81DFD92795F1FD8D7415C05367B922472255C02F78B0194AB086918CA7)
* 将选中颜色、字体、间距和图标提取为资源（Resource）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/xRRVVyf6QDK5ROa9m4kJlA/zh-cn_image_0000002791841094.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=882F36A65A346E16CF1E139FA4554B485B542E4CB21949BF144318821ADFDEC9)
* 将选中的代码块或完整语句提取为方法/函数（Method）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/uTaDj59BRBmoMPPkFGzwjw/zh-cn_image_0000002820681025.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=230830150B33A2F4A801E0A4D404BF8EEB20B63528D8EBF595FBEECC9D7EDF86)

  在ArkTS语言中，也支持将组件调用代码块提取为@Builder装饰器装饰方法，组件属性调用表达式则可提取为@Styles或@Extend装饰器装饰方法。选中需要提取的组件或属性，右键单击**重构**，选择**提取函数**，组件私有属性可提取为@Extend装饰的方法，通用属性可提取为@Styles或@Extend装饰的方法。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/KKl9uYfuRPWS7Z9Ui7Nxyw/zh-cn_image_0000002791841108.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=F22A6AA3576DDB3A3D6D7527E65C2EEF62FDB168140C2C0295D107267FE0BA23)
* 将选中的对象自变量提取为接口（Interface）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/qhJFSpvZSRmQGJj3F8QFLg/zh-cn_image_0000002792001080.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=AED1819D5FD383F589BFF9A371BE20B6580915B42759207E3C0D3CF6B0A30A0A)

### 代码转换

编辑器内提供Convert重构能力，支持Convert between named imports and namespace imports等高频转换操作，辅助开发者高效重构代码，提升代码质量。

**表1** Refactor-Convert功能支持清单

| 功能 | 说明 | 使用方法 | 支持转换的源码类型 |
| --- | --- | --- | --- |
| Convert to class | 将JS源码中的function转换为符合ES6标准的类 | 点击或选中function名，右键单击**重构> 转换**，在弹窗中选择转换的方式。 | JS |
| Convert to anonymous function | 将箭头函数转换为匿名函数 | 选中箭头函数赋值变量，右键单击**重构> 转换**，在弹窗中选择转换的方式。 | JS/TS |
| Convert to named function | 将箭头函数转换为普通函数 | 选中箭头函数赋值变量，右键单击**重构> 转换**，在弹窗中选择转换的方式。 | JS/TS/ArkTS |
| Convert to arrow function | 将匿名函数转换为箭头函数 | 选中匿名函数赋值变量，右键单击**重构 > 转换**，在弹窗中选择转换的方式。 | JS/TS/ArkTS |
| Convert default export to named export | 支持named export和default export相互转换 | 完整选中export default语句，右键单击**重构 > 转换**，在弹窗中选择转换的方式。 | JS/TS/ArkTS |
| Convert named export to default export | 完整选中export语句，右键单击**重构 > 转换**，在弹窗中选择转换的方式。 |
| Convert named imports to namespace import | 支持在命名import和命名空间import形态间转换 | 完整选中import语句，右键单击**重构 > 转换**，在弹窗中选择转换的方式。 | JS/TS/ArkTS |
| Convert namespace import to named imports | 完整选中命名空间import语句，右键单击**重构 > 转换**，在弹窗中选择转换的方式。 |
| Convert to template string | 将字符串转换为模板字面量 | 选中字符串或完整表达式，右键单击**重构 > 转换**，在弹窗中选择转换的方式。 | JS/TS/ArkTS |
| Convert to optional chain expression | 将判空逻辑转换为可选链式调用 | 选中连续判空表达式，右键单击**重构 > 转换**，在弹窗中选择转换的方式。 | JS/TS/ArkTS |

## C++代码重构

编辑器提供C++代码重构能力，当前支持交换if分支、添加using声明等使用场景下的重构能力，提升开发效率。

### 交换if分支

编辑器支持在选中if-else完整代码块的情况下，实现对if-else代码块的位置交换，并对条件取反。

**使用约束**

* 需要重构的代码块必须为完整的if-else代码结构，{}不能省略；
* if-else中的statement包含嵌套if-else语句时，只反转最外层的if-else语句。对于if() -else if()-else() 结构，仅支持对最后一层if-else结构进行交换；
* 不支持赋值语句的判断条件取反。

**使用方式**

编辑器内选择需要转换的代码区域，右键单击**重构** > **代码操作**，选择**Swap if branches**，对原有if条件取反，并交换if-else原代码块顺序。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/bJXlXDtDQX2_vSijYMVw9w/zh-cn_image_0000002792001074.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6F5DC6602F35F9E511DDB3D3B57E9EB2B991B39D5EB0FE0F5FF3F7C6A6F8240)

### 将语句转为原始字符串

编辑器提供重构能力，支持将带有 \n, \t, \", \\, \'五类转义字符的字符串转换为原始字符串。当前仅支持标准字符串，不支持 u8""等其他字符串。

在编辑器内选择字符串代码区域，右键单击**重构 > 代码操作**，选择**Convert to raw string**，将语句转换为原始字符串。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/P85h5g9wRt6dCtE8NtGDiQ/zh-cn_image_0000002792001082.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=E8A83D6FAEFA1C634E9BA7A0D3BF18661C316DBA158E318F4D85BF5B3A049038)

### 定义构造函数

编辑器提供重构能力，支持为类的成员变量生成默认的构造函数。

**规格限制**

1. 不支持未初始化成员变量的类
2. 不支持在（class标识符，类名，大括号）以外的位置触发
3. 不支持类已存在有入参的构造函数

**使用方法：**在类的定义的类名处，右键单击**重构** > **代码操作**，选择**Define constructor**，为成员变量定义一个构造函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/XH1uzPj0To2io9zFbUVRpg/zh-cn_image_0000002820721031.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=93C57E4B4161D39F3935121C07CB1131F2468D05B43F430A12380FEA245B5EAB)

### 提取表达式到变量

在编辑器内，选中需要提取的表达式范围，右键单击**重构 > 代码操作**，选择**Extract subexpression to variable**，支持提取表达式到变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/BpiC2v4XTmKOTwCc9LtdLg/zh-cn_image_0000002820721039.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B06F57FA5573941617CAB633E7304354C51C3B1CBB5F6492224DE911C334ECE)

### 移除namespace

光标停留在需要移除的namespace处，右键单击**重构 > 代码操作**，选择**Remove using namespace, re-qualify names instead**进行移除，可以避免命名冲突，提高代码可读性。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/Rl9cuBexSn6JTLXj0dZ7Dw/zh-cn_image_0000002792001078.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=395DF17ADD6236FE3B81230930BE36ACECA1CCA887DA350AFC0927E16839A984)

### 添加using声明

编辑器内，光标停留在需要添加using声明处，右键单击**重构 > 代码操作**，选择**Add using-declaration for ff and remove qualifier**完成使用using定义类型别名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/_Uxi4X_dSxO8OeANArWPww/zh-cn_image_0000002792001072.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D3D7FD2668720BE3A8FE76C012ACC0A0700B6B371F837B8D6E4CE787816708D)

### auto自动展开

在auto关键字处右键单击**重构 > 代码操作**，选择**Replace with deduced type**，可以使用推断类型替换auto类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/zz2ekzxcSm-z4ylMp5-IKQ/zh-cn_image_0000002820721033.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=87F99AD00E3AC265FC4CCE4E308673C30B81A11C991BF290B82855B9218D26B3)

### 声明隐式成员

编辑器支持在类中声明隐式复制/移动成员。光标停留在需要生成的类处，右键单击**重构 > 代码操作**, 选择**Declare implicit copy/move members**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/bANYeuYPSKm9353-J0Nhsw/zh-cn_image_0000002820681043.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=79E09828C8524F4EBCE1330E1681ABD065260DEEDADFFEA7A90BFBC2ED63106D)
