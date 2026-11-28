---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-next-code-refactoring
title: 代码重构
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码重构
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:55+08:00
doc_updated_at: 2026-11-23
content_hash: sha256:6d9bb4e3511856480a3cc85d979dbd96f41d19ea3c64338032a2078bd9946881
---

## ArkTS/TS代码重构

### 安全删除

编辑器支持安全删除功能，帮助开发者安全地删除代码中的标识符对象（变量、函数或类等）或删除指定文件。在删除前，编辑器会先在代码中搜索对该对象的引用，如果存在引用，编辑器将提示开发者进行必要的检查和调整。

**使用方式：**在编辑器内选中需要删除的标识符对象，右键单击**重构**，选择**安全删除**，单击**确认**后将自动检查当前对象在代码中被引用的情况，点击**查看引用**可查看具体使用的代码内容，点击**删除**将直接删除该对象的定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/svhNiD7ER5WKGlObW_lixw/zh-cn_image_0000002820721037.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=D25B7714931178763808C44E8D1747384895DD01E7AB66D7A2CE14F7A36109F0)

### 代码重命名

代码编辑支持重命名功能，可以快速更改变量、函数、类、类成员等相关标识符及文件、文件夹的名称，并同步到整个工程中对其进行引用的位置。

**使用方式：**选中需要重新命名的标识符（变量、类、接口、函数等），右键单击**重构 > 重命名**（或快捷键**Shift+F6**），在弹框中输入新的标识符名称，点击**重命名**完成变量重命名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/ES3BE92yQb-N8hNY7M9hdw/zh-cn_image_0000002820681029.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=FFCF385A4ED444C21B997596BAFCC20C7967B9D8C0E1E3D897FFB9F9B4818542)

代码重命名支持预览功能。在**重命名**弹窗中点击**预览**，编辑器左侧的预览列表中查看变量被引用的位置。

**说明** 

若ArkTS文件中存在C++接口调用，使用Rename进行重命名时，C++文件中涉及的函数名也会被重命名。

### 代码提取

在编辑器中支持将函数内、类方法内等区域代码块或表达式，提取为新变量（Variable）、方法/函数（Method）、常量（Constant）、接口（Interface）、变量（Variable）或类型别名（Type Alias）。准确便捷地将所选区域代码从当前作用域内进行提取，提升编码效率。选中所需要提取的代码块，右键单击**重构**，选择需要提取的类型。

* 将选中的表达式提取为变量（Variable）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/22LcThvFQSeR7jqmK8IOOQ/zh-cn_image_0000002820681037.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=73215D65B55C02F644E81B990A1987611F71521115D1FD6C0ED16279BBF07724)
* 将选中的单行表达式提取为常量（Constant）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/VYD2PMIfRVmdUPEZ_eByIA/zh-cn_image_0000002792001068.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBDE597F3264C7BD51F79EE8066B30A195DB07E69F09235FD2436E9CD04E9582)
* 将选中颜色、字体、间距和图标提取为资源（Resource）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/5bRK5BBlSWSPGeaKdldzzQ/zh-cn_image_0000002791841094.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B4EE82C598E364CAB459FA51EF70AB54E7E8B17E925774A38AFAC53044DD3A0)
* 将选中的代码块或完整语句提取为方法/函数（Method）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/uuDGud8hTTqvDzPHX24heQ/zh-cn_image_0000002820681025.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB77ACEC7EBC1A509AD4A98264BD65B77F33B69E837734079AED671D24708747)

  在ArkTS语言中，也支持将组件调用代码块提取为@Builder装饰器装饰方法，组件属性调用表达式则可提取为@Styles或@Extend装饰器装饰方法。选中需要提取的组件或属性，右键单击**重构**，选择**提取函数**，组件私有属性可提取为@Extend装饰的方法，通用属性可提取为@Styles或@Extend装饰的方法。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/YiUyr5PYRKSIaeGMjyaOoA/zh-cn_image_0000002791841108.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=D48BC63FB50822742BAB4A0C0E22B1694D5836EAEA43692C76300C4536B08FCF)
* 将选中的对象自变量提取为接口（Interface）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/ap0y-WGTQuiyMAXtVclZOQ/zh-cn_image_0000002792001080.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=B425D8655E215DC77CA7FD34778F6DC7395192F0AEC32D4A00B155F43ABEEBE4)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/KDo9yzKNTn6XW9BhsQRj2Q/zh-cn_image_0000002792001074.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF4C40F03A8E6030923EE2B53100F9AAFE6C6DD38EABBBE46142565DCC030C34)

### 将语句转为原始字符串

编辑器提供重构能力，支持将带有 \n, \t, \", \\, \'五类转义字符的字符串转换为原始字符串。当前仅支持标准字符串，不支持 u8""等其他字符串。

在编辑器内选择字符串代码区域，右键单击**重构 > 代码操作**，选择**Convert to raw string**，将语句转换为原始字符串。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/wofwVSFZS1mCm1mMINfl7w/zh-cn_image_0000002792001082.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=75E214E5A356D150DF979EE2BEC55D612128B6B28B8F3CD095369621EAEA97A1)

### 定义构造函数

编辑器提供重构能力，支持为类的成员变量生成默认的构造函数。

**规格限制**

1. 不支持未初始化成员变量的类
2. 不支持在（class标识符，类名，大括号）以外的位置触发
3. 不支持类已存在有入参的构造函数

**使用方法：**在类的定义的类名处，右键单击**重构** > **代码操作**，选择**Define constructor**，为成员变量定义一个构造函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/67NVp5AYSO-v73YKy1aBsA/zh-cn_image_0000002820721031.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=F8574911D9319C26546C0BC224A7040B0ECDFCF206DDF962AA0719F73FC4EBA9)

### 提取表达式到变量

在编辑器内，选中需要提取的表达式范围，右键单击**重构 > 代码操作**，选择**Extract subexpression to variable**，支持提取表达式到变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/EuZtrr6cTWW9qknnAANG9Q/zh-cn_image_0000002820721039.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B383D553CFCA8FB8EAE221EA092D57C77EA338C2350F0D37BCA63061ECAFB2A)

### 移除namespace

光标停留在需要移除的namespace处，右键单击**重构 > 代码操作**，选择**Remove using namespace, re-qualify names instead**进行移除，可以避免命名冲突，提高代码可读性。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/zq8PspUETbyD8hm_KnqmjQ/zh-cn_image_0000002792001078.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=78028FB7B11CEEB843EF2ADD30465C7B2F2ADC8C14FBDDC65139CB0298070DBE)

### 添加using声明

编辑器内，光标停留在需要添加using声明处，右键单击**重构 > 代码操作**，选择**Add using-declaration for ff and remove qualifier**完成使用using定义类型别名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/Os_zErU7SvuoPjTz45LB0Q/zh-cn_image_0000002792001072.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=C14B1E60A8C3E5D68210B72F50DDF3BAC765882D4AE802088FB0333BB6D33F62)

### auto自动展开

在auto关键字处右键单击**重构 > 代码操作**，选择**Replace with deduced type**，可以使用推断类型替换auto类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/vmOt92t8TL6BFRgxtjWyEw/zh-cn_image_0000002820721033.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E409BD4487D26D685E9D5D31ACE0C51D6D8208FEF90EA9DD6BD137239FAE5BF)

### 声明隐式成员

编辑器支持在类中声明隐式复制/移动成员。光标停留在需要生成的类处，右键单击**重构 > 代码操作**, 选择**Declare implicit copy/move members**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/HQEm0EITQMi-2XHF-WA4Ew/zh-cn_image_0000002820681043.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=10321332838A424EE6CB4120BC07E40C1345032D78527B6441F7B653C291A1A1)
