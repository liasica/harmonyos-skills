---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-4
title: 编译报错“Cannot find module XXX or its corresponding type declarations”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Cannot find module XXX or its corresponding type declarations”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:08+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:4dde597f2733c5730e8379622e38d310af18afd6542ca0e98d38e8ece22f50b5
---

* **场景一：**

  **问题现象**

  Stage模板工程编译引用native文件(.so) 提示“Cannot find module XXX or its corresponding type declarations.”。

  **解决措施**

  当前Stage工程在编译构建阶段新增对native文件（.so）导出符号的语法校验。如果现有工程引用了没有对应声明文件（.d.ts）的native文件（.so），语法校验工具会报错，提示找不到对应的声明文件。

  如果出现类似问题，尝试以下解决方法：

  1. 在对应cpp目录下新建types/libxxx目录，并在该目录下新增index.d.ts用于声明native文件的类型符号；新增oh-package.json5配置文件用于校验工具的模块查询。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/0nywl8TURKqy3mE5AIixYg/zh-cn_image_0000002229604373.png?HW-CC-KV=V1&HW-CC-Date=20260428T002907Z&HW-CC-Expire=86400&HW-CC-Sign=FFA956221A8DA047DA22F01712D77D4E06D15A3A9EBEA471C92DC87DD467187F)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/BPTvHjBVR-y-gT4Qhi9hrw/zh-cn_image_0000002194158980.png?HW-CC-KV=V1&HW-CC-Date=20260428T002907Z&HW-CC-Expire=86400&HW-CC-Sign=EFB09AF072195CE7AB0F7672726D462BA1B040E6155D72328F87EF739FFB7D0B)
  2. 在native文件引用的模块内的oh-package.json5中添加native文件的本地依赖，并根据DevEco Studio提示点击\*\*Sync Now\*\*同步工程，下图以entry模块引用native文件为例。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/3qbSwyLgSFW_oOxbxgPHmA/zh-cn_image_0000002194318572.png?HW-CC-KV=V1&HW-CC-Date=20260428T002907Z&HW-CC-Expire=86400&HW-CC-Sign=702F5D2125107BB63C4D6738B3A3B2DF50EDC2358A3230BD1499A088B42614CC)

* **场景二：**

  **问题现象**

  API 11 Stage模板工程编译失败，提示“Cannot find module '@kit.xxx' or its corresponding type declarations”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/ug8AYAWVQZeHe7s-QN7svg/zh-cn_image_0000002229758849.png?HW-CC-KV=V1&HW-CC-Date=20260428T002907Z&HW-CC-Expire=86400&HW-CC-Sign=EF22E95F2AAEF25AEAEA928A487CEF0F23E647DB73AB29AA20DB726A8D9096D4)

  **问题原因**

  出现该问题的原因是使用DevEco Studio NEXT Developer Preview1及之后版本。新创建的API 11 Stage模型的模板文件中，import方式改为import xxx from '@kit.xxx'。若SDK使用的是HarmonyOS NEXT Developer Preview1之前的版本，将会出现编译报错，因为旧的SDK不支持此类方式导入。

  **解决措施**

  如果出现类似问题，需要对SDK进行更新或更新DevEco Studio。

  + 如果使用的是DevEco Studio NEXT Developer Preview1至HarmonyOS NEXT Developer Beta1（5.0.3.300）之间的版本，在菜单栏点击**Tool > SDK Manager**，将SDK更新至HarmonyOS NEXT Developer Preview1及以上版本后，重新进行编译。
  + 如果使用的是HarmonyOS NEXT Developer Beta1（5.0.3.300）及以上的版本，SDK随DevEco Studio软件包安装，无需单独下载，请在[下载中心](https://developer.huawei.com/consumer/cn/download/)下载并使用新版本DevEco Studio。
* **场景三：**

  **问题现象**

  引用第三方包，构建失败，提示“Cannot find module 'xxx' or its corresponding type declarations”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/hV3j4xkNRpejYzfDKeOeqw/zh-cn_image_0000002229758853.png?HW-CC-KV=V1&HW-CC-Date=20260428T002907Z&HW-CC-Expire=86400&HW-CC-Sign=2A0CE6D05B828ADCDA311D86F3745480D4657618F3EECB28490902C801B30AD9)

  **解决措施**

  进入模块级或工程级的oh-package.json5文件，检查第三方包是否已安装。若未安装，执行ohpm install安装。若已安装，检查“main”字段是否配置正确。若未配置或配置错误，需配置为正确的入口文件。
* **场景四：**

  **问题现象**

  包路径被混淆，代码中又是在引用包路径后面拼接了路径，导致模块引用不到而报错。

  例如：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/msRhOhtESMOs2DJDvfJemw/zh-cn_image_0000002194158984.png?HW-CC-KV=V1&HW-CC-Date=20260428T002907Z&HW-CC-Expire=86400&HW-CC-Sign=1E656886FF0B340DD389C2E8D29B8342FCBC2D3A912A52D7D75BD00466E1ADF0)

  代码中这样引用

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/N6JgifJ9QkC8HNeTDKJLHQ/zh-cn_image_0000002229758861.png?HW-CC-KV=V1&HW-CC-Date=20260428T002907Z&HW-CC-Expire=86400&HW-CC-Sign=D05A4B874D56C9C7D19B40E16388861C80A44D7079030D294046D4A5D94AE637)这样引用会找不到模块，导致报错。

  **解决措施**

  修改引用方式，采用推荐的方式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/x-WmboZXS9ysOFn9vjcewA/zh-cn_image_0000002194158972.png?HW-CC-KV=V1&HW-CC-Date=20260428T002907Z&HW-CC-Expire=86400&HW-CC-Sign=172E14FA8E1265043C2E4C4416F318040B9C0063F9CAAF83556001072FAFB879)
* **场景五：**

  **问题现象**

  被引用模块oh-package.json5配置有误，执行了ohpm install 并且成功地安装了依赖，但是还报错模块找不到。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/z9vVSX6iQ0m41azj9PwGeg/zh-cn_image_0000002194158976.png?HW-CC-KV=V1&HW-CC-Date=20260428T002907Z&HW-CC-Expire=86400&HW-CC-Sign=42D500A319F62C72268C0DE57F21D8A1D4494A825EB24D8E2FD177243A73F72D)

  被引用模块的 oh-package.json5 中配置了错误的types字段。

  该字段优先于main字段。 如果 types 字段配置的不存在，就会报错模块找不到。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/RqN-TOi9TLaHXKg0EmWg1A/zh-cn_image_0000002229604353.png?HW-CC-KV=V1&HW-CC-Date=20260428T002907Z&HW-CC-Expire=86400&HW-CC-Sign=2E4A1F6AABFBED04C18E3DEB048E099AD63F15FF6AAF0357F79972F3FBC1DFD1)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/9i2FoN5KSQO7jE2kcz_FfQ/zh-cn_image_0000002229758841.png?HW-CC-KV=V1&HW-CC-Date=20260428T002907Z&HW-CC-Expire=86400&HW-CC-Sign=13CF47CCBD798940FE658E80210A80BA20996E2D2BDE2C623252BE3CD8341724)

  **解决措施**

  该问题源于工程引用了无对应实现文件的.d.ts声明文件。

  1. 在build目录搜索`rollup\_plugin\_ignore\_empty\_module\_placeholder`定位问题模块。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/nDr8vPz7RHehPvyxEjT3zA/zh-cn_image_0000002194158956.png?HW-CC-KV=V1&HW-CC-Date=20260428T002907Z&HW-CC-Expire=86400&HW-CC-Sign=A3686EC348701F31B2DC6A966A11081CD3EB4DDCB9FE75CFBAFDBC717222CC05)

     在输入栏中输入“rollup\_plugin\_ignore\_empty\_module\_placeholder”，找到问题模块的中间文件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/T8rq9CEYTzi8tOZvBV_ZUw/zh-cn_image_0000002194158964.png?HW-CC-KV=V1&HW-CC-Date=20260428T002907Z&HW-CC-Expire=86400&HW-CC-Sign=5055C6A638353325AD8E30EE0E069DD815060B126E842D247040453E718E8185)
  2. 在引用类型文件中通过添加type显式声明符号类型。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/26kSvc89SbOoT4hxR6-nzw/zh-cn_image_0000002229758865.png?HW-CC-KV=V1&HW-CC-Date=20260428T002907Z&HW-CC-Expire=86400&HW-CC-Sign=4BBC0D6F863B43F9D6DDB8439826C0F1B001B0FA01A89F5BCBF799B5AE076F46)
  3. 同时排查是否从d.ts/d.ets中引用值类型符号。禁止在声明文件中声明值变量。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/ZpJMwK_BTJC6wp8Wzo6_7g/zh-cn_image_0000002194158968.png?HW-CC-KV=V1&HW-CC-Date=20260428T002907Z&HW-CC-Expire=86400&HW-CC-Sign=3724DED8F3D57DDADBB4BA34BB2B3BC548ED6B915680FA351EFEE9D68F4DDB80)
