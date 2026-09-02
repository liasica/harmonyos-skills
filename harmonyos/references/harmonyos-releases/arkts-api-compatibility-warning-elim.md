---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/arkts-api-compatibility-warning-elim
title: ArkTS API兼容性保护
breadcrumb: 版本说明 > 应用升级适配与兼容性 > 应用兼容性说明 > 应用开发中的兼容性场景开发指导 > API兼容性保护和告警屏蔽 > ArkTS API兼容性保护
category: harmonyos-releases
scraped_at: 2026-09-02T14:59:08+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2305884cce6063b0db93693c5bcf48224fa7e616bd32603f8468d0c3f6421aeb
---

## 简介

随着HarmonyOS 持续迭代，为确保持续兼容老版本用户，开发者常需设置较低的compatibleSdkVersion。但这可能导致应用在低版本系统上因调用未受保护的新 API 而崩溃（如低版本设备误调高版本接口）。为了解决这一痛点，帮助开发者在调用新 API 时做好版本隔离，我们提供了以下几种兼容性保护的最佳实践。

从API version 26.0.0版本开始，推荐使用apiAvailable接口，进行兼容性判断保护。

## 通过apiAvailable接口兼容性保护

### 接口定义和用途

**接口定义**：

```screen
apiAvailable(version: string | number): boolean;
```

检查指定的API版本在当前设备上是否可用，会根据输入格式和API版本范围自动选择合适的版本检查方法。

apiAvailable 接口运行结果仅包含两种返回状态：返回 true 时，代表传入的版本号适配当前设备运行环境、接口能力可用；返回 false 时，代表传入的版本号不适配当前设备运行环境，或接口传入参数格式不符合规范。

**请参考：**[apiavailable API参考](../harmonyos-references/js-apis-device-info.md#deviceinfoapiavailable)。

使用示例：

* 针对API version 26.0.0及以后的版本，使用apiAvailable接口进行兼容性判断保护。

  ```screen
  import { deviceInfo } from '@kit.BasicServicesKit';

  function getTestData(): void {
    if (deviceInfo.apiAvailable('26.0.0')) {
    // 调用26.0.0的API新接口
    } else {
    // 降级方案
    }
  }
  ```

* 针对API version 26.0.0之前的HarmonyOS设备独有特性接口，即接口标记为since M.S.F(N)（文档中标记“起始版本：M.S.F(N)”, SDK物理包中hms路径下所包含的接口），使用apiAvailable接口进行兼容性判断保护。

  ```screen
  import { deviceInfo } from '@kit.BasicServicesKit';

  //针对HarmonyOS专有接口，即接口标记为since M.S.F(N)的接口
  function getTestData(): void {
    // 传入参数时不带括号中的版本
    if (deviceInfo.apiAvailable('5.0.1')) {
    // 调用API版本5.0.1(13)的API新接口 
    } else {
    // 降级方案
    }
  }
  ```
* 针对API version 26.0.0之前的OpenHarmony底座接口，即接口标记为since N（文档中标记“起始版本：N”，SDK物理包中openharmony路径下所包含的接口），使用apiAvailable接口进行兼容性判断保护。

  ```screen
  import { deviceInfo } from '@kit.BasicServicesKit';

  //针对OpenHarmony底座公共接口，即接口标记为since N
  function getTestData(): void {
    if (deviceInfo.apiAvailable(22)) {
    // 调用22的API新接口
    } else {
    // 降级方案
    }
  }
  ```

### 接口使用规格限制说明

1. **apiAvailable入参版本规格校验**。
   * **OpenHarmony工程**

     传入版本号为整数，0 < X < 26。

     传入版本号为X.Y.Z语义化版本格式，X >= 26，0 <= Y <= 99，0 <= Z <= 99。
   * **HarmonyOS工程**

     传入版本号为整数，0 < X < 26。

     传入版本号为X.Y.Z语义化版本格式，X > 0，0 <= Y <= 99，0 <= Z <= 99（X < 26时，需确认HarmonyOS闭源版本号是否支持，否则编译报错）。
2. **请严格遵循该接口的推荐调用方式，在接口参数中以字面量形式直接写入版本号，可在编译阶段及时校验并发现版本号书写错误。若采用变量传参等其他调用方式传入版本号参数，将无法在编译期识别版本号书写异常问题。**

   **使用正例**

   ```typescript
   import { deviceInfo } from '@kit.BasicServicesKit';
   function getTestData(): void {
     if(deviceInfo.apiAvailable('6.1.1')) { // 使用字面量版本号，编译阶段会校验版本号是否正确
       // 调用6.1.1的接口。
     }
   }
   ```

   **使用反例：**

   ```typescript
   import { deviceInfo } from '@kit.BasicServicesKit';
   function getTestData(): void {
     let format_error_version: string = '6.1.01'; // 使用错误的版本号格式传入参数，编译无提示。版本号不允许出现前导0，应该改成6.1.1。
     if(deviceInfo.apiAvailable(format_error_version)) { // 运行时返回false，格式错误
       // 调用6.1.1的接口。
     }
     let not_exist_version: string = '6.1.3'; // 使用不存在的版本号传入参数，编译无提示。
     if(deviceInfo.apiAvailable(not_exist_version)) { // 运行时根据设备实际版本号返回结果，不校验闭源HarmonyOS版本号是否存在
       // 调用6.1.3的接口。
     }
   }
   ```
3. **告警消除功能仅支持在if语句中****，不支持自定义封装，不支持以变量赋值形式传入版本参数****，必须传入规范版本号(纯字面量)写法**。

   使用反例：

   ```screen
   import { deviceInfo } from '@kit.BasicServicesKit';

   class BbClass {
     version: string = '27.0.0';
   }
   function getTestData(): void {
     // 告警消除不支持类赋值
     const Bb: BbClass = new BbClass();
     if (deviceInfo.apiAvailable(Bb.version)) {
     // 调用27.0.0的API新接口  
     }
     //告警消除不支持自定义封装
     let result:boolean =  deviceInfo.apiAvailable('26.0.0');
     if(result) {
     // 调用26.0.0的API新接口    
     }
   }
   ```
4. **告警消除功能仅支持在if语句中，if 判断不支持三元表达式写法，不支持逻辑符号复合判断，例如：'&&'、 '||'、 '!'等**。

   使用反例：

   ```typescript
   import { deviceInfo } from '@kit.BasicServicesKit';

   function getTestData(): void {
     // 告警消除不支持逻辑非。
     if(!deviceInfo.apiAvailable('26.0.0')) {
       // 调用26.0.0的API新接口   
     }
     // 告警消除不支持逻辑且。
     if(deviceInfo.apiAvailable('26.0.0') && deviceInfo.softwareModel == 'ALN-AL00') {
       // 调用26.0.0的API新接口   
     }
     // 告警消除不支持逻辑或。
     if(deviceInfo.apiAvailable('26.0.0') || deviceInfo.apiAvailable(24)) {
       // 调用26.0.0的API新接口   
     }
     // 告警消除不支持三元表达式。
     if(deviceInfo.softwareModel == 'ALN-AL00' ? deviceInfo.apiAvailable('26.0.0') : deviceInfo.apiAvailable('27.0.0')) {
       // 调用对应的API新接口   
     }
     // 告警消除不支持逻辑符复合。
     if(deviceInfo.apiAvailable('26.0.0') && deviceInfo.softwareModel == 'ALN-AL00' || deviceInfo.apiAvailable('26.0.0') && deviceInfo.softwareModel == 'ALN-AL00') {
       // 调用26.0.0的API新接口   
     }
   }
   ```

### 重要说明

* 对于应用能力的兼容性判断，建议使用面向开发者相关的API版本接口（例如：apiAvailable接口）。
* HarmonyOS设备中"设置 > 点击设备名称 > 关于本机"中显示的各种版本号信息中，开发者只需要关注**API版本**信息。
* 开发者不应该使用面向消费者的HarmonyOS版本信息去进行应用能力兼容性判断（例如distributionOSVersion或displayVersion等字段返回的版本号实际为设备ROM版本号，与开发者严格使用的API版本号并无严格的关联关系，无法保证与API版本号一一对应）。
* 应注意，deviceInfo.sdkApiVersion仅能用于OpenHarmony底座接口的兼容性保护。

### 示例一：HdsActionBar组件适配

**场景描述**：应用操作栏（ActionBar）在不同系统版本下的兼容性适配方案。场景中，支持点击操作栏中间的按钮，进行切换图标及展开和收起操作栏。

代码通过判断设备的distributionOSApiVersion是否达到6.0.0(20)（对应的值为60000）来实现适配：在高版本系统（6.0.0(20)及以上）中，直接使用UIDesignKit提供的HdsActionBar组件，利用其原生支持的startButtons、endButtons配置项快速构建操作栏，而在低版本系统中，采用Row容器与基础Button组件组合的降级方案，通过条件渲染模拟按钮的展开和收起状态，并用基本点击事件实现图标切换逻辑，确保核心交互功能在低版本设备上仍可正常使用。

```screen
import { HdsActionBar, ActionBarButton, ActionBarStyle } from '@kit.UIDesignKit';
import { deviceInfo } from '@kit.BasicServicesKit';

@Component
export struct ActionBarAdapter {
  @State isExpand: boolean = true;
  @State isPrimaryIconChanged: boolean = false;
  build() {
    Column() {
      if (deviceInfo.apiAvailable(20)) {
        // 调用6.0.0(20)版本API的组件。
        HdsActionBar({
          startButtons: [new ActionBarButton({
            baseIcon: $r('sys.symbol.stopwatch_fill')
          })],
          endButtons: [new ActionBarButton({
            baseIcon: $r('sys.symbol.mic_fill')
          })],
          primaryButton: new ActionBarButton({
            baseIcon: $r('sys.symbol.plus'),
            altIcon: $r('sys.symbol.play_fill'),
            onClick: () => {
              this.isExpand = !this.isExpand;
              this.isPrimaryIconChanged = !this.isPrimaryIconChanged;
            }
          }),
          actionBarStyle: new ActionBarStyle({
            isPrimaryIconChanged: this.isPrimaryIconChanged
          }),
          isExpand: this.isExpand!!
        })
      } else {
        // 降级计划
        Row({ space: 25 }) {
          if (this.isExpand) {
            Button({ type: ButtonType.Circle }) {
              SymbolGlyph($r('sys.symbol.stopwatch_fill'))
                .fontSize(24)
                .fontColor([$r('sys.color.font_secondary')])
            }
            .aspectRatio(1)
            .height(45)
            .backgroundColor($r('sys.color.background_secondary'))
            .margin({ left: 10 })
          }
          Button({ type: ButtonType.Circle }) {
            SymbolGlyph(this.isExpand ? $r('sys.symbol.plus') : $r('sys.symbol.play_fill'))
              .fontSize(24)
              .fontColor([$r('sys.color.white')])
          }
          .aspectRatio(1)
          .height(55)
          .backgroundColor($r('sys.color.brand'))
          .onClick(() => {
            this.isExpand = !this.isExpand;
          })
          if (this.isExpand) {
            Button({ type: ButtonType.Circle }) {
              SymbolGlyph($r('sys.symbol.mic_fill'))
                .fontSize(24)
                .fontColor([$r('sys.color.font_secondary')])
            }
            .aspectRatio(1)
            .height(45)
            .backgroundColor($r('sys.color.background_secondary'))
            .margin({ right: 10 })
          }
        }
        .backgroundColor($r('sys.color.background_primary'))
        .borderRadius(30)
      }
    }
    .width('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
  }
}
```

### 示例二：Scroll组件缩放功能适配

**场景描述**：在图片浏览类应用（如相册或电商商品详情页）的开发中，通常需要实现图片的缩放查看功能。Scroll组件的缩放功能（如设置最大/最小缩放比例以及弹性缩放效果）需要较高的系统API Level支持（API 20及以上版本）。

为了确保应用在低版本系统上不会因调用不支持的API而崩溃，同时在高版本系统上能提供更丰富的交互体验，可以通过设备API Level判断来动态启用这些高级功能。

在本示例中，创建了一个自定义属性修饰器MyModifier，在其applyNormalAttribute方法中检查当前设备的sdkApiVersion。当检测到设备版本符合要求（API Level≥20）时，才会为Scroll容器设置缩放相关的属性（maxZoomScale, minZoomScale, enableBouncesZoom）。这样，高版本设备用户可以享受流畅的图片缩放体验，而低版本设备用户则仍能正常浏览图片，只是无法进行缩放操作，从而实现了兼容性适配。

```screen
import { deviceInfo } from '@kit.BasicServicesKit';

class MyModifier implements AttributeModifier<ScrollAttribute> {
  applyNormalAttribute(instance: ScrollAttribute): void {
    // 根据设备信息中的API版本信息进行判断
    if (deviceInfo.apiAvailable(20)) {
      // 为了适应滚动条的缩放属性，可以设置最小和最大缩放比例。
      instance.maxZoomScale(1.2)
        .minZoomScale(0.5)
        .enableBouncesZoom(true)
    }
  }
}
@Component
export struct ScrollComponentAdapter {
  adaptModifier: MyModifier = new MyModifier();
  build() {
    Scroll() {
      // 'app.media.image1' 只是一个示例，请替换为实际的图片。
      Image($r('app.media.startIcon'))
    }
    .scrollable(ScrollDirection.FREE)
    .width('100%')
    .attributeModifier(this.adaptModifier)
  }
}
```

### 示例三：Text组件跑马灯效果适配

**场景描述**：在新闻资讯或实时信息展示类应用中，经常需要实现文字跑马灯（Marquee）效果，以便在有限空间内展示较长的文本内容（如新闻标题或重要通知）。Text组件的跑马灯功能需要API 18及以上版本才能支持。

为了确保应用在低版本系统上正常运行，同时在高版本系统上提供更生动的视觉效果，需要根据设备版本动态启用此特性。

本示例展示了如何通过版本判断实现文本跑马灯功能的条件式启用。通过自定义属性修饰器MyModifier，在applyNormalAttribute()方法中检查设备API Level。当设备版本达到18或以上时，才会为Text组件设置文本溢出模式为跑马灯（TextOverflow.MARQUEE）并启动滚动效果（marqueeOptions）。这样，高版本设备用户可以看到动态滚动的文字效果，增强信息展示的吸引力，而低版本设备用户则看到静态文本（可能会被截断或显示为省略号），保证了基础的信息可读性，实现了功能体验与兼容性的平衡。

```screen
import { deviceInfo } from "@kit.BasicServicesKit";

class MyModifier implements AttributeModifier<TextAttribute> {
  applyNormalAttribute(instance: TextAttribute): void {
    // 根据设备信息中的API版本信息进行判断
    if (deviceInfo.apiAvailable(18)) {
      // 当设备版本达到18或以上时，Text组件设置文本溢出模式为跑马灯。
      instance.textOverflow({ overflow: TextOverflow.MARQUEE })
        .marqueeOptions({ start: true })
    }
  }
}
@Component
export struct TextComponentAdapter {
  private message: string = 'This a simple Code of Text Marquee';
  private adaptModifier: MyModifier = new MyModifier();
  build() {
    Text(this.message)
      .fontSize(24)
      .height(200)
      .width('100%')
      .attributeModifier(this.adaptModifier)
  }
}
```

## 通过@Available注解标注最低适用版本

在API 22之前版本，开发者仅能通过手动编写注释文本的方式标注方法的最低适用版本，这种方式存在版本约束传递不精准的问题。为此，系统提供**@Available**注解，助力开发者更规范、高效地管控API的调用过程的版本依赖场景。当然**@Available**本身提供的特性不只是为了提供消除兼容性告警，而是让开发者通过@Available标注相关接口，然后根据自己的业务需求再去对需要标注的接口本身的行为进行判断。

### 使用说明

**@Available注解参数**：

* minApiVersion表示API最低引入版本，由系统类型和版本号组成。
* 在OpenHarmony工程中使用时，minApiVersion字段不支持填写HarmonyOS。

  例如，在HarmonyOS工程中支持的配置：

  @Available({minApiVersion: '22'})、@Available({minApiVersion: 'OpenHarmony 22'})、@Available({minApiVersion: 'HarmonyOS 6.0.2'})

  在OpenHarmony工程中支持的配置：

  @Available({minApiVersion: '22'})、@Available({minApiVersion: 'OpenHarmony 22'})

**@Available声明周期**：

源码级注解，仅参与编译过程。

**@Available使用限制**：

* 可以标注在变量声明、类型声明（struct、class、interface、typeAlias、enum）、函数声明、命名空间声明、注解声明以及struct、class、interface的成员上。
* 不可以标注在非声明式元素上。

### 校验逻辑

编译器依据项目配置的compatibleSdkVersion进行校验，若该版本低于被注解API的引入版本，编译器将触发兼容性告警，提示低版本系统运行时可能因调用未存在的 API 导致崩溃。

**告警示例**：

```screen
The 'commonPrintUtil' API is available since SDK version 22. However, the current compatible SDK version is 5.0.3(15).
It is recommended to use apiAvailable to safeguard API compatibility.
```

### 正反示例

**HarmonyOS工程正例**：

```screen
import { Available } from '@kit.BasicServicesKit';

// 表示该API在API version 22及以上的OpenHarmony兼容设备可用。
@Available({minApiVersion: 'OpenHarmony 22'}) class testClassA {}
@Available({minApiVersion: '22'}) // 表示该API在API version 22及以上的OpenHarmony兼容设备可用。
class testClassB {}
@Available({minApiVersion: 'HarmonyOS 6.0.2'}) // 表示该API在版本为6.0.2(22)及以上的HarmonyOS兼容设备可用。
class testClassC {}
```

**语义化版本正例**：

```screen
import { Available } from '@kit.BasicServicesKit';

@Available({minApiVersion: '26.0.0'}) // 表示该API在26.0.0及以上的HarmonyOS兼容设备可用。
class testClassD {}
@Available({minApiVersion: '27.0.0'}) // 表示该API在27.0.0及以上的HarmonyOS兼容设备可用。
class testClassE {}
```

**HarmonyOS工程反例**：

```screen
import { Available } from '@kit.BasicServicesKit';

// 版本号校验异常,OpenHarmony 版本号正确格式为1-999的整数
// 编辑和编译有如下报错：The runtime OS for the current project is HarmonyOS. The OS version number 9999 is invalid. The OpenHarmony version must be an integer between 1 and 999, and when the OpenHarmony version is greater than or equal to 26, the version number format also supports the M.S.F format.
@Available({minApiVersion: '9999'})
class testClassA {}
// 版本号校验异常，HarmonyOS的版本号正确格式为M.S.F，M的范围为1-99的整数，S的范围为0-99的整数，F的范围为0-99的整数。
// 编辑和编译产生报错：...The HarmonyOS version must follow the M.S.F format, where M is an integer between 1 and 99, and S and F are integers between 0 and 99.
@Available({minApiVersion: 'HarmonyOS 6.0.2.0'})
class testClassB {}
// 系统类型校验异常，HarmonyOS工程目前仅支持HarmonyOS和OpenHarmony
// 编辑和编译产生报错：The runtime OS for the current project is HarmonyOS. @Available is not supported on the OS: OpenHarmonyNew.
@Available({minApiVersion: "OpenHarmonyNew 22"})
class testClassC {}
```

**OpenHarmony工程正例**：

```screen
import { Available } from '@kit.BasicServicesKit';

@Available({minApiVersion: 'OpenHarmony 22'}) // 表示该API在API version 22及以上的OpenHarmony兼容设备可用。
class testClassA {}
@Available({minApiVersion: '22'}) //表示该API从API version为22及以上的OpenHarmony兼容设备是可用的。
class testClassB {}
```

**OpenHarmony工程反例**：

```screen
import { Available } from '@kit.BasicServicesKit';

// 版本号校验异常，OpenHarmony 版本号正确格式为1-999的整数
// 编辑和编译产生报错：The runtime OS for the current project is HarmonyOS. The OS version number 9999 is invalid. The OpenHarmony version must be an integer between 1 and 999, and when the OpenHarmony version is greater than or equal to 26, the version number format also supports the M.S.F format.
@Available({minApiVersion: '9999'})
class testClassA {}
// OSName校验异常，OpenHarmony工程目前使用@Available注解时，注解参数中的系统类型只支持OpenHarmony
// 编辑和编译产生报错：The runtime OS for the current project is OpenHarmony. @Available is not supported on the OS: HarmonyOS.
@Available({minApiVersion: 'HarmonyOS 6.0.2'})
class testClassB {}
// 系统类型校验异常，OpenHarmony工程目前使用@Available注解时，注解参数中的系统类型只支持OpenHarmony
// 编辑和编译产生报错：The runtime OS for the current project is OpenHarmony. @Available is not supported on the OS: OpenHarmonyNew.
@Available({minApiVersion: "OpenHarmonyNew 22"})
class testClassC {}
```

### 场景示例

应用开发者在使用其他开发者提供的API时，可以通过查看其@Available注解来判断该API是否能在自己应用所支持的最低系统版本上运行。

当应用开发者提供有版本约束的API给其他开发者（例如通过 HAR 包）使用时，也应该在提供的API上使用@Available注解，以标明这些API是在哪个系统版本中引入的。

**场景**

当应用开发者在版本迭代中新增调用系统能力的公共API时，需通过@Available注解为该API标注最低可用版本。当API调用方的运行环境版本低于注解中声明的最低版本要求时，编译及编辑阶段会触发兼容性告警，提示开发者注意版本适配问题。针对此类兼容性告警，调用方可通过使用兼容性告警消除的几种方式消除告警提示。

**提供方示例**

```screen
import { Available } from '@kit.BasicServicesKit';

@Available({minApiVersion: '22'})
export function commonPrintUtil(): void {
  // 调用6.0.2(22)版本的新接口
}
```

**调用方示例**

```screen
import { Available, deviceInfo } from '@kit.BasicServicesKit';
// commonPrintUtil需导入提供方的接口定义文件。
import { commonPrintUtil} from '../../util';

// 不建议写法：如果HarmonyOS工程根目录下build-profile.json5文件设置的compatibleSdkVersion值小于22，假设当前HarmonyOS工程的compatibleSdkVersion是5.0.3(15)
// 直接调用开发者自定义function且没有做版本判断处理，编译器会在开发者自定义function调用处抛出告警，提示该方法可能在低版本设备上运行失败

function businessFuncA(): void {
  commonPrintUtil(); // 告警：The 'commonPrintUtil' API is available since SDK version 22. However, the current compatible SDK version is 5.0.3(15).
}
// 建议写法1：使用deviceInfo.sdkApiVersion获取系统软件API版本进行判断，可以避免低版本设备运行异常，消除编译告警
function businessFuncB(): void {
  if (deviceInfo.sdkApiVersion >= 22) {
    commonPrintUtil();
  } else {
    // 根据业务处理
  }
}
// 建议写法2：在开发者自定义function调用处的父级函数（或类）上，标记@Available起始版本信息，当新标记的版本号不低于 开发者自定义function的最低可用版本, 消除编译告警
@Available({minApiVersion: '22'})
function businessFuncC(): void {
  commonPrintUtil();
}
```

**语义化版本场景示例**

**提供方：标注26.0.0新增的API**

```screen
import { Available } from '@kit.BasicServicesKit';

@Available({minApiVersion: '26.0.0'})
export function newFeature26(): void {
  // 26.0.0新增的API实现
}
```

**调用方：使用apiAvailable兼容性保护判断**

```screen
import { deviceInfo } from '@kit.BasicServicesKit';
// newFeature26需导入提供方的接口定义文件。
import { newFeature26 } from '../../util';

function caller() {
  if (deviceInfo.apiAvailable('26.0.0')) {
    newFeature26();
  } else {
    // 降级方案
  }
}
```
