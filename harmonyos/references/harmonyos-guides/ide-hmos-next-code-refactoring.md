---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-next-code-refactoring
title: 代码重构
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码重构
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:16+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:8fe71b091dd90f204beecb30e2b89038e7f76f2b344f0f5105ed9851dd414362
---

## ArkTS/TS代码重构

### 安全删除

编辑器支持安全删除功能，帮助开发者安全地删除代码中的标识符对象（变量、函数或类等）或删除指定文件。在删除前，编辑器会先在代码中搜索对该对象的引用，如果存在引用，编辑器将提示开发者进行必要的检查和调整。

**使用方式：**在编辑器内选中需要删除的标识符对象，右键单击**重构**，选择**安全删除**，单击**确认**后将自动检查当前对象在代码中被引用的情况，点击**查看引用**可查看具体使用的代码内容，点击**删除**将直接删除该对象的定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/x8FltuLMQw-gawu3x02Tlw/zh-cn_image_0000002810630759.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=762AB2926F6CD0F8101A65CA6BEA304C777C91498DF4389EA734D9AA2C425865)

### 代码重命名

代码编辑支持重命名功能，可以快速更改变量、函数、类、类成员等相关标识符及文件、文件夹的名称，并同步到整个工程中对其进行引用的位置。

**使用方式：**选中需要重新命名的标识符（变量、类、接口、函数等），右键单击**重构 > 重命名**（或快捷键**Shift+F6**），在弹框中输入新的标识符名称，点击**重命名**完成变量重命名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/Eo8TRrfETDqQgUY0x4v93g/zh-cn_image_0000002781311278.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=B06823C1EF5F44D5F35BC83147FF6E503E59BD64727BF0851A795500A316A05D)

代码重命名支持预览功能。在**重命名**弹窗中点击**预览**，编辑器左侧的预览列表中查看变量被引用的位置。

**说明** 

若ArkTS文件中存在C++接口调用，使用Rename进行重命名时，C++文件中涉及的函数名也会被重命名。

### 代码提取

在编辑器中支持将函数内、类方法内等区域代码块或表达式，提取为新变量（Variable）、方法/函数（Method）、常量（Constant）、接口（Interface）、变量（Variable）或类型别名（Type Alias）。准确便捷地将所选区域代码从当前作用域内进行提取，提升编码效率。选中所需要提取的代码块，右键单击**重构**，选择需要提取的类型。

* 将选中的表达式提取为变量（Variable）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/zrIci25HSImsQlP8lY_BFA/zh-cn_image_0000002781311284.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=EFE363676A6F4DE44CC798AD0815FED643E1C0628EECED517B688AF919C86A94)
* 将选中的单行表达式提取为常量（Constant）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/9_SyLNKXRpSXdCTThnOLZg/zh-cn_image_0000002810750867.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=20C1600F655FC4595AA955825DB7DCC9BAA2A2EE423DAB1088567A4C089B09E7)
* 将选中颜色、字体、间距和图标提取为资源（Resource）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/cYFXj5B_QxeSrcXfhDLWCA/zh-cn_image_0000002810750869.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=12150D5166F81ECC2B9BB590D4292326D5D0ACF6043FB25DDD32DB163C00BB46)
* 将选中的代码块或完整语句提取为方法/函数（Method）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/7rdr6choS1eFaeGgmi6w-A/zh-cn_image_0000002810750873.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C233B058C23BB13413BD7B381132D94742EF09E39DCD9A24F1486E65EA7AB99)

  在ArkTS语言中，也支持将组件调用代码块提取为@Builder装饰器装饰方法，组件属性调用表达式则可提取为@Styles或@Extend装饰器装饰方法。选中需要提取的组件或属性，右键单击**重构**，选择**提取函数**，组件私有属性可提取为@Extend装饰的方法，通用属性可提取为@Styles或@Extend装饰的方法。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/cOcfoG_iSgmr5v1PoftdXA/zh-cn_image_0000002810630761.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=76BD5190C727A03DEC0D2738E73CABB5E40F214ECB4EBCC5D1AE3C73D6C4967A)
* 将选中的对象自变量提取为接口（Interface）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/dbEy48VhRDyTfPRoEJ_Sgw/zh-cn_image_0000002810630763.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E68D0A7AB6CA7E70BEF3DCAB7B13734223B6233FC7242F887F13C1A6DA989D7)

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
| Convert to optional chain expression | 将判空逻辑转换为可选链式调用 | 选中连续判 空表达式，右键单击**重构 > 转换**，在弹窗中选择转换的方式。 | JS/TS/ArkTS |

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/g_2TiUeJTR6bjkJdJ0T_4A/zh-cn_image_0000002781311286.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F1006ECBF737ADC8650C29D0D5676B486585DAC5D711B7CE51F4EC4F9E59C55)

### 将语句转为原始字符串

编辑器提供重构能力，支持将带有 \n, \t, \", \\, \'五类转义字符的字符串转换为原始字符串。当前仅支持标准字符串，不支持 u8""等其他字符串。

在编辑器内选择字符串代码区域，右键单击**重构 > 代码操作**，选择**Convert to raw string**，将语句转换为原始字符串。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/fxbvvAdIS3WsOhVfZ6K8VQ/zh-cn_image_0000002781471212.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=C742D3D5C881428BCB7A7092F1D03FF1CF3BA798186C222C0819DDF35798C8CC)

### 定义构造函数

编辑器提供重构能力，支持为类的成员变量生成默认的构造函数。

**规格限制**

1. 不支持未初始化成员变量的类
2. 不支持在（class标识符，类名，大括号）以外的位置触发
3. 不支持类已存在有入参的构造函数

**使用方法：**在类的定义的类名处，右键单击**重构** > **代码操作**，选择**Define constructor**，为成员变量定义一个构造函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/wf_n_uXITC-mNwQO7_4_jw/zh-cn_image_0000002810750877.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6C1F79F971B383A933E0C0DB4B107F2C08949AAEE8070957B6F0E4B2186F193)

### 提取表达式到变量

在编辑器内，选中需要提取的表达式范围，右键单击**重构 > 代码操作**，选择**Extract subexpression to variable**，支持提取表达式到变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/fafHT-yqQfe0kxhT_ABeZQ/zh-cn_image_0000002810630767.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB5F1C3F13D2DF367479B628E04987303805E1470E5CA84509DAE48294773347)

### 移除namespace

光标停留在需要移除的namespace处，右键单击**重构 > 代码操作**，选择**Remove using namespace, re-qualify names instead**进行移除，可以避免命名冲突，提高代码可读性。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/GbGESOYHTOGQDrihh2JqAQ/zh-cn_image_0000002781311282.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC57380A2838166C9133A7D6F6462917C36BA97D5A95650B47D54EB1CBEA8493)

### 添加using声明

编辑器内，光标停留在需要添加using声明处，右键单击**重构 > 代码操作**，选择**Add using-declaration for ff and remove qualifier**完成使用using定义类型别名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/itBS51XFSgSTRfzn-fvW_g/zh-cn_image_0000002781471216.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=781CC7BC9285E9A20F38238E5EC8254483B0DB1E0BE268826C86B13D37114578)

### auto自动展开

在auto关键字处右键单击**重构 > 代码操作**，选择**Replace with deduced type**，可以使用推断类型替换auto类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/G0qbDqTSSl6hiddXwLa9Mg/zh-cn_image_0000002810750879.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E502B77500FFDBC170F74D91EBECF74EAE6C1B8756B2957823018F411A37F4E)

### 声明隐式成员

编辑器支持在类中声明隐式复制/移动成员。光标停留在需要生成的类处，右键单击**重构 > 代码操作**, 选择**Declare implicit copy/move members**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/-kAblpfaT-GlYwKtIn95yA/zh-cn_image_0000002810750871.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=25CFB608967E0CEABF25F23452213CF23A9B311C697352CA093ABDBFBFA282C7)
