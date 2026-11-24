---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-run-debug-configurations
title: 自定义运行/调试配置
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 自定义运行/调试配置
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:35b371cc694fe5da02eee6f257ef7739ca25381012d0cd93ac76e72bb47dca36
---

## 配置应用可调试

应用是否支持调试，根据app.json5的debug字段和build-profile.json5的debuggable字段综合判断，app.json5的优先级高于build-profile.json5。

1. 在app.json5中配置debug字段：
   * true：应用支持调试。
   * false：应用不支持调试。
2. 如果没有配置debug字段，则根据build-profile.json5的debuggable字段判断应用是否支持调试。
   * true：应用支持调试。当[构建模式](ide-hmos-hvigor-compilation-options-customizing-guide.md#section192461528194916)不是release时，debuggable的缺省值是true，即支持调试。
   * false：应用不支持调试。当构建模式为release时，debuggable的缺省值是false，即不支持调试。

## 设置调试代码类型

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/jKpFR6EeSLa1tN26Nic4uA/zh-cn_image_0000002820681195.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F3BAE7136E5A6F185CDD65BAD9FA5694F876A17A86F303954DFA11E1CD0AC3E "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/WXFpKFt_QzWU6aGWW3FEtQ/zh-cn_image_0000002820721199.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=0128C279CFA0A8E480848950F627AE54E81C8F07B9069DEAC87977DCD127F530 "点击放大")按钮打开配置界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/1EuNcdQeQ-GzoVJGqn7e1w/zh-cn_image_0000002820721195.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=3ECADC484F3AA5D0B955ADF2CF962C2BFDFD6F6A138B1E3379377A7FAF41875B)

在配置界面中点击**调试器**选项并设置**调试类型**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/sLkIV8cuRDuQpLsR9PHXAw/zh-cn_image_0000002820721191.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF433B31AE05C1B2B4DF9B66AE66FF2D2B54A06742E4F3A0D2A013037099236D)

工程调试类型默认为Detect Automatically，关于各调试类型的说明如下表所示：

**表1** 调试类型配置项

| 调试类型 | 调试代码 |
| --- | --- |
| **Detect Automatically** | 新建工程默认调试器选项。根据工程模块及其依赖的模块涉及的编程语言，自动启动对应的调试器。 |
| **ArkTS/JS** | * 调试ArkTS代码 * 调试JS代码 |
| **Native** | 仅调试C/C++代码 |
| **Dual(ArkTS/JS + Native)** | 调试C/C++工程的ArkTS/JS和C/C++代码 |

## 设置HAP安装方式

在调试阶段，HAP在设备上的安装方式有2种，可以根据实际需要进行设置。

* 安装方式一：先卸载应用/元服务后，再重新安装。该方式会清除设备上应用/元服务所有的缓存数据。

  DevEco Studio支持当代码无变化时，不进行推包安装。即根据模块有无变化来判断是否重新推送安装模块包，在运行调试时仅将有变化的模块及依赖它的模块重新推送安装至设备上。如entry依赖了HSP模块，当HSP模块有变化，运行调试时将同时推送安装HSP模块和entry模块。
* 安装方式二：采用覆盖安装方式，不卸载应用/元服务，该方式会保留应用/元服务的缓存数据。

设置方法如下：

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/5rAxwpzvTpWQS5ggfkOXiA/zh-cn_image_0000002820681193.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=25173A1A6162CA911B706B303EF18FEB9EF6371BD30EF79F5ADF49D2D4C7C828 "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/K4rIobwSQKOj3sjqKF8HMg/zh-cn_image_0000002792001234.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=C282D06E2FD7C1EFF8299198F74B437FB27553C038E5E830087CDF8B48AB457A "点击放大")按钮打开配置界面。在配置界面**通用**中设置指定模块的HAP安装方式，勾选**保留应用数据**，则表示采用覆盖安装方式，保留应用/元服务缓存数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/TRH7tdrVShKmDKq1gVs_ww/zh-cn_image_0000002791841256.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D09DF58B55822488BB07F7DAA2059A8E0EFDBC50049FCD6C5CE7A6507EC5D30)

### 配置自定义调试参数

如果未进行自定义，将按默认配置安装和运行应用。如果开发者需要对应用安装、运行等流程增加参数配置，可在**安装参数**和**启动参数**下进行配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/gH-WzSFBSRWb15C-pc607Q/zh-cn_image_0000002792001230.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=D70BEB539C34EE0521848CBCDEA09368E6E5973DE031219916C531D2F7A1867F)

* **安装参数**
  + **启用源码行跳转**：勾选**启用源码行跳转**表示在构建产物中系统组件增加debugline属性，用于开启[ArkUI 界面检查器源码跳转功能](ide-hmos-arkui-inspector.md#section44774145517)。
  + **安装标志**：输入bm install命令相关的选项，请参见[bm install 参数](bm-tool.md#安装命令install)。如设置"-w 360"，表示将超时等待时间设置为360秒。
* **启动参数**
  + **启动**：指定在安装应用后启动的Ability。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/JKnj00MJRbOxOwyzBhMHkw/zh-cn_image_0000002791841260.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=2DCD55A8CE49173BDE829AE6D5A588C74030FC2A0A36823DC5DFBD85464A137F)

    - **空**：只安装不启动任何Ability。
    - **默认 Ability**：默认的EntryAbility，即module.json5文件中配置了“skills”属性的第一个ability；若无配置“skills”属性的ability，则取“mainElement”指定的ability（该ability需存在于“abilities”数组内）；若“mainElement”未指定，则取“abilities”数组内的第一个ability。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/k9ChcLl5THO5ndG41C_JYw/zh-cn_image_0000002792001236.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6C014A4BBDB9223F3205717E431D5B838F747223D37C3221348055CC961E8F7 "点击放大")
    - **指定 Ability**：工程中的UIAbility或ExtensionAbility。

      可以在工程中添加UIAbility或ExtensionAbility，详细请参阅[UIAbility开发指导](uiability.md)或[ExtensionAbility开发指导](extensionability-overview.md)。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/zznOtObORZeTS-Bv9meAFg/zh-cn_image_0000002820681189.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3C663B8B494164C6C1B5105C45E2D04D8F7B1EF4DC3B02D6BD50251A31283FE)
  + **启动标志**：输入aa start命令相关的选项，请参见[aa start 参数](aa-tool.md)。

### 配置环境变量

如果开发者需要配置和管理应用开发环境，以及控制应用程序的行为，可配置环境变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/6eT3UQg-SmKGN8DEKgkgUg/zh-cn_image_0000002820721201.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=DBD53CFCB62FDE2F8D7CEBA514322BE663087AEBC7982C39CA211A8CCD185811)

点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/yQXqWZ0nS2uNWho-DFt0jQ/zh-cn_image_0000002820681197.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=9DE143E039E4826C9EF09E3100A37C3019F460A60ED66590430F5D9DF82A95E1)按钮，新增一行配置项。当前支持以下配置项：

* ASAN\_OPTIONS：在运行时配置ASan的行为，包括设置检测级别、输出格式、内存错误报告的详细程度等，具体可配置的value请参见[配置参数](../best-practices/bpta-stability-asan-detection.md#section1496994494018)。若开发者未配置log\_exe\_name、abort\_on\_error，DevEco Studio将自动填充。ASAN\_OPTIONS是应用级别的，只在entry和feature模块中配置生效，HAR/HSP模块配置不生效。

**说明** 

当配置环境变量后，**保留应用数据**覆盖安装不生效。

环境变量配置完成后，需确保环境变量已勾选。

## 多模块调试

### 安装多个模块

如果一个工程中同一个设备存在多个模块（如存在entry和feature模块），且存在模块间的调用时，在调试阶段需要同时安装多个模块的Hap包到设备中。此时，需要在**多包推送**中选择多个模块，启动调试时，DevEco Studio会将所有的模块都安装到设备上。

设置方法如下：

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/ij_oCf6cSOiyT-qidKT9Kg/zh-cn_image_0000002820681199.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=CE4FABF95DC803BEE08A5443812AB7948A0AF91BA9AE5F5C87619D3C8FC221CB "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/6YB-IdQsTTu2t4Y_wy_gwg/zh-cn_image_0000002820721205.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4D30AB56F1E1DE51EEB8E35481718A57B53C7DD8B79D1321471CC575C3F7578 "点击放大")按钮打开配置界面。在配置界面**通用**中，勾选**多包推送**，选择多个模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/EKU9J_jmRjiY1rQNHjIVzw/zh-cn_image_0000002791841250.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=728F1E154E40B136BF126EFA771238DBD392BA4979E0F3569BDC1DF559067749)

### 自动安装依赖

如果一个工程中entry/feature/HSP模块直接依赖其他HAR/HSP模块（如entry模块依赖HSP模块）及间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块），在调试阶段需要同时安装模块包及其所有依赖模块的包到设备中，此时，可以设置**自动依赖**，启动调试时会自动将所有依赖的模块都安装到设备上。

设置方法如下：

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/T5fZ7gOGSP6pcItuFnej_Q/zh-cn_image_0000002820721207.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=5697677380148290F2746C699A1E0930A642511CE8AA59FC8A0903FFA845E444 "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/7CxIgeSRRTCuILEl3OrtpQ/zh-cn_image_0000002791841258.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=81C3BB74882B0C0251FFD77CBD8A2D43F7E462CDE1F7CB59077808EC2288F3BD "点击放大")按钮打开配置界面。在配置界面**通用**中，勾选**自动依赖。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/74jiW-r2QpWFGjIWSdzFRQ/zh-cn_image_0000002791841262.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=D7CA980377B8711030098D7E57E5C8A95ABAC3751877DD58640634E50A348D43)

在**前置任务**中，可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/cLCgMM5GTyyfHYWnaKHRBQ/zh-cn_image_0000002792001232.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9265F8E8E8D612934F23F5A1716EAF566AC52C97EC7EDB4BC5686742F2E5A4A "点击放大")添加应用启动前的任务，也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/QUPtYPFRToqhNK6pGOnSng/zh-cn_image_0000002792001238.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=7121C69F5AE947180584B9B48B872B426734926432DEF51CB4CB883CA2E43ED5 "点击放大")移除任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/p4uRrACpS168DbcHs1MXRw/zh-cn_image_0000002791841264.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=69BE242D80022FA23A4B9C393A6737FB0359A014FC9F099581FC728F32896538 "点击放大")

在勾选**自动依赖**后，可以同时勾选**多包推送**，从而达到推送所有包的效果。
