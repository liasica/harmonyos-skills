---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-4
title: 编译报错“Cannot find module XXX or its corresponding type declarations”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Cannot find module XXX or its corresponding type declarations”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:f433667e6ddbf61e08df3d27271a7705b23ceef55e31ada72b28703923ba9ff7
---

* **场景一：**

  **问题现象**

  Stage模板工程编译引用native文件(.so) 提示“Cannot find module XXX or its corresponding type declarations.”。

  **解决措施**

  当前Stage工程在编译构建阶段新增对native文件（.so）导出符号的语法校验。如果现有工程引用了没有对应声明文件（.d.ts）的native文件（.so），语法校验工具会报错，提示找不到对应的声明文件。

  如果出现类似问题，尝试以下解决方法：

  1. 在对应cpp目录下新建types/libxxx目录，并在该目录下新增index.d.ts用于声明native文件的类型符号；新增oh-package.json5配置文件用于校验工具的模块查询。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/fWxgFzuCSXGzesG2zID9Lg/zh-cn_image_0000002654837773.png)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/HJGIDx5RRdO8-c8dnqBvJA/zh-cn_image_0000002624478464.png)
  2. 在native文件引用的模块内的oh-package.json5中添加native文件的本地依赖，并根据DevEco Studio提示点击\*\*Sync Now\*\*同步工程，下图以entry模块引用native文件为例。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/n5vQyiGUSP6mptEor36Vcw/zh-cn_image_0000002654797827.png)

* **场景二：**

  **问题现象**

  API 11 Stage模板工程编译失败，提示“Cannot find module '@kit.xxx' or its corresponding type declarations”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/1tUYv8vCRPabbuGLQXPx_A/zh-cn_image_0000002624638370.png)

  **问题原因**

  出现该问题的原因是使用DevEco Studio NEXT Developer Preview1及之后版本。新创建的API 11 Stage模型的模板文件中，import方式改为import xxx from '@kit.xxx'。若SDK使用的是HarmonyOS NEXT Developer Preview1之前的版本，将会出现编译报错，因为旧的SDK不支持此类方式导入。

  **解决措施**

  如果出现类似问题，需要对SDK进行更新或更新DevEco Studio。

  + 如果使用的是DevEco Studio NEXT Developer Preview1至HarmonyOS NEXT Developer Beta1（5.0.3.300）之间的版本，在菜单栏点击**Tool > SDK Manager**，将SDK更新至HarmonyOS NEXT Developer Preview1及以上版本后，重新进行编译。
  + 如果使用的是HarmonyOS NEXT Developer Beta1（5.0.3.300）及以上的版本，SDK随DevEco Studio软件包安装，无需单独下载，请在[下载中心](https://developer.huawei.com/consumer/cn/download/)下载并使用新版本DevEco Studio。
* **场景三：**

  **问题现象**

  引用第三方包，构建失败，提示“Cannot find module 'xxx' or its corresponding type declarations”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/GnOBkMNSQN6ntDXYAe8X1g/zh-cn_image_0000002654837775.png)

  **解决措施**

  进入模块级或工程级的oh-package.json5文件，检查第三方包是否已安装。若未安装，执行ohpm install安装。若已安装，检查“main”字段是否配置正确。若未配置或配置错误，需配置为正确的入口文件。
* **场景四：**

  **问题现象**

  包路径被混淆，代码中又是在引用包路径后面拼接了路径，导致模块引用不到而报错。

  例如：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/kTo5yFSrRO-Gr2OrNeRNoQ/zh-cn_image_0000002624478466.png)

  代码中这样引用

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/geIvx9ZKTfqX6bHZBDYWug/zh-cn_image_0000002654797829.png)这样引用会找不到模块，导致报错。

  **解决措施**

  修改引用方式，采用推荐的方式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/e2kClQxkQ5C4Sps9iYGz8Q/zh-cn_image_0000002624638372.png)
* **场景五：**

  **问题现象**

  被引用模块oh-package.json5配置有误，执行了ohpm install 并且成功地安装了依赖，但是还报错模块找不到。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/Hqui-g5ORh-udmlPEAcAEg/zh-cn_image_0000002654837777.png)

  被引用模块的 oh-package.json5 中配置了错误的types字段。

  该字段优先于main字段。 如果 types 字段配置的不存在，就会报错模块找不到。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/BBgotMbATNiZN861wWzLzQ/zh-cn_image_0000002624478468.png)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/ZNHm_7VpQPGHgdGyJa3KTg/zh-cn_image_0000002654797831.png)

  **解决措施**

  该问题源于工程引用了无对应实现文件的.d.ts声明文件。

  1. 在build目录搜索`rollup\_plugin\_ignore\_empty\_module\_placeholder`定位问题模块。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/0hLkPEZuTPSI7oSR9Mt1iA/zh-cn_image_0000002624638374.png)

     在输入栏中输入“rollup\_plugin\_ignore\_empty\_module\_placeholder”，找到问题模块的中间文件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/jdheP4tDQUiFwDEruUVDhg/zh-cn_image_0000002654837779.png)
  2. 在引用类型文件中通过添加type显式声明符号类型。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/EGJfBJPDSuewFAV_tkjP1w/zh-cn_image_0000002624478470.png)
  3. 同时排查是否从d.ts/d.ets中引用值类型符号。禁止在声明文件中声明值变量。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/BIbpP21DRm-6yPkpp1pEcw/zh-cn_image_0000002654797833.png)
