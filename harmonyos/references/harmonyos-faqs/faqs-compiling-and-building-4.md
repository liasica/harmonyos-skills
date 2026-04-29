---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-4
title: 编译报错“Cannot find module XXX or its corresponding type declarations”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Cannot find module XXX or its corresponding type declarations”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:22+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:93a95e16e2366b2dfda7aa7e79034695b1299875765f6412ccb16135b3c87608
---

* **场景一：**

  **问题现象**

  Stage模板工程编译引用native文件(.so) 提示“Cannot find module XXX or its corresponding type declarations.”。

  **解决措施**

  当前Stage工程在编译构建阶段新增对native文件（.so）导出符号的语法校验。如果现有工程引用了没有对应声明文件（.d.ts）的native文件（.so），语法校验工具会报错，提示找不到对应的声明文件。

  如果出现类似问题，尝试以下解决方法：

  1. 在对应cpp目录下新建types/libxxx目录，并在该目录下新增index.d.ts用于声明native文件的类型符号；新增oh-package.json5配置文件用于校验工具的模块查询。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/0nywl8TURKqy3mE5AIixYg/zh-cn_image_0000002229604373.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=12E6A96021BC4A0A52FD028C224EABD1709D7B3B4790944FFADE83DB272DB109)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/BPTvHjBVR-y-gT4Qhi9hrw/zh-cn_image_0000002194158980.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=D4B07185FE7202BFE45E9494C29CBB758D29E66DD24C29F8470F1AE8ACF081AB)
  2. 在native文件引用的模块内的oh-package.json5中添加native文件的本地依赖，并根据DevEco Studio提示点击\*\*Sync Now\*\*同步工程，下图以entry模块引用native文件为例。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/3qbSwyLgSFW_oOxbxgPHmA/zh-cn_image_0000002194318572.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=05363A069462F99CBA5DF258C59DF917B887516B742CC74B6CEB1B46B347B5D5)

* **场景二：**

  **问题现象**

  API 11 Stage模板工程编译失败，提示“Cannot find module '@kit.xxx' or its corresponding type declarations”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/ug8AYAWVQZeHe7s-QN7svg/zh-cn_image_0000002229758849.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=BFF445C0111C1E059FCA5D0CB2F17C1B4B149D39DA1242F12E64BF589F47C5B5)

  **问题原因**

  出现该问题的原因是使用DevEco Studio NEXT Developer Preview1及之后版本。新创建的API 11 Stage模型的模板文件中，import方式改为import xxx from '@kit.xxx'。若SDK使用的是HarmonyOS NEXT Developer Preview1之前的版本，将会出现编译报错，因为旧的SDK不支持此类方式导入。

  **解决措施**

  如果出现类似问题，需要对SDK进行更新或更新DevEco Studio。

  + 如果使用的是DevEco Studio NEXT Developer Preview1至HarmonyOS NEXT Developer Beta1（5.0.3.300）之间的版本，在菜单栏点击**Tool > SDK Manager**，将SDK更新至HarmonyOS NEXT Developer Preview1及以上版本后，重新进行编译。
  + 如果使用的是HarmonyOS NEXT Developer Beta1（5.0.3.300）及以上的版本，SDK随DevEco Studio软件包安装，无需单独下载，请在[下载中心](https://developer.huawei.com/consumer/cn/download/)下载并使用新版本DevEco Studio。
* **场景三：**

  **问题现象**

  引用第三方包，构建失败，提示“Cannot find module 'xxx' or its corresponding type declarations”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/hV3j4xkNRpejYzfDKeOeqw/zh-cn_image_0000002229758853.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=22C518EB5993A3F04011E8DF2FD822706EED9D984C538E212C958968834E4E6C)

  **解决措施**

  进入模块级或工程级的oh-package.json5文件，检查第三方包是否已安装。若未安装，执行ohpm install安装。若已安装，检查“main”字段是否配置正确。若未配置或配置错误，需配置为正确的入口文件。
* **场景四：**

  **问题现象**

  包路径被混淆，代码中又是在引用包路径后面拼接了路径，导致模块引用不到而报错。

  例如：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/msRhOhtESMOs2DJDvfJemw/zh-cn_image_0000002194158984.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=768822355E765329FA1F571A67400E37A5CBE764D12308E9219B9D415034AFAA)

  代码中这样引用

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/N6JgifJ9QkC8HNeTDKJLHQ/zh-cn_image_0000002229758861.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=BA55FE6FFEA014A39F0AD6272D2B41C1E62170219B90E1F4222BDC82F083A992)这样引用会找不到模块，导致报错。

  **解决措施**

  修改引用方式，采用推荐的方式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/x-WmboZXS9ysOFn9vjcewA/zh-cn_image_0000002194158972.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=E6EE5FFC61B5FB34A11D03069F87D6AD042D6A7B9B7CCD5B1D8B6BC29B1AE6A9)
* **场景五：**

  **问题现象**

  被引用模块oh-package.json5配置有误，执行了ohpm install 并且成功地安装了依赖，但是还报错模块找不到。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/z9vVSX6iQ0m41azj9PwGeg/zh-cn_image_0000002194158976.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=D24C4FBE5551011B20B96EA5A258F3971A07BF82F3343C5932A10A18C820BDDA)

  被引用模块的 oh-package.json5 中配置了错误的types字段。

  该字段优先于main字段。 如果 types 字段配置的不存在，就会报错模块找不到。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/RqN-TOi9TLaHXKg0EmWg1A/zh-cn_image_0000002229604353.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=D867B99CB94A160EFF7BBD065C8A20CE95B411900A01E9B2D1B7A5C25AE0ACFB)

  **解决措施**

  如果该包中没有d.ets声明，可以删除这个字段。配置错误或不存在会导致报错。
* **场景六：**

  **问题现象**

  oh-package.json5中dependencies中引入模块的名称和实际使用时import的不一致。

  在代码中“import”时，应使用大写的“HAR”而不是“dependencies”里配置的“har”。务必保持完全一致，否则在Linux系统中会报错，提示模块找不到。

  **解决措施**

  引入和使用改成一致。
* **场景七：**

  **问题现象**

  引用模块的oh-package.json5中main字段值和实际的文件名称大小写不一致。

  **解决措施**

  将main字段和实际文件名称大小写改为一致。
* **场景八**：

  **问题现象**

  Stage模板工程编译构建失败，提示“Cannot find module '@bundle:rollup\_plugin\_ignore\_empty\_module\_placeholder' or its corresponding type declarations”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/9i2FoN5KSQO7jE2kcz_FfQ/zh-cn_image_0000002229758841.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=B872582345507A98B611E47C65048549C64A24344C2175FAD22DDCE2076A15A8)

  **解决措施**

  该问题源于工程引用了无对应实现文件的.d.ts声明文件。

  1. 在build目录搜索`rollup\_plugin\_ignore\_empty\_module\_placeholder`定位问题模块。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/nDr8vPz7RHehPvyxEjT3zA/zh-cn_image_0000002194158956.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=8028F83448C555CAE4B2D97A82A4B833F86D1226D886628FF09D33350893E7B2)

     在输入栏中输入“rollup\_plugin\_ignore\_empty\_module\_placeholder”，找到问题模块的中间文件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/T8rq9CEYTzi8tOZvBV_ZUw/zh-cn_image_0000002194158964.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=4C61D987558E84A53FEFB0248BF9E31FB829BFC5145261A22A348B70B6BB95E1)
  2. 在引用类型文件中通过添加type显式声明符号类型。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/26kSvc89SbOoT4hxR6-nzw/zh-cn_image_0000002229758865.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=E79C7FEF634C442CA19DC432BF06DE9624D7AEE017AE256EBBB9E850C6EF11B3)
  3. 同时排查是否从d.ts/d.ets中引用值类型符号。禁止在声明文件中声明值变量。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/ZpJMwK_BTJC6wp8Wzo6_7g/zh-cn_image_0000002194158968.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=8050FC871CE1A6EA68652203F87060C5A4B5868D794110CE5EFF904EFD9C4FC3)
