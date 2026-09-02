---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/app-compatibility-third-har
title: 应用集成三方库（har包）的兼容性指导
breadcrumb: 版本说明 > 应用升级适配与兼容性 > 应用兼容性说明 > 应用开发中的兼容性场景开发指导 > 应用集成三方库（har包）的兼容性指导
category: harmonyos-releases
scraped_at: 2026-09-02T14:59:08+08:00
doc_updated_at: 2026-07-06
content_hash: sha256:07fab71a038a1da50727e699f04017b31a0ee717010a5925d4a3426b78ae28d2
---

**说明** 

API版本号格式从26.0.0开始进行调整（详见[版本号格式调整说明](version-number-26.md)），不影响对API兼容性判断的基本逻辑，因此在文档的示意性描述中暂时仍保持旧版本格式的说明。

近期API版本号的大小关系如下：

26.0.0 > 6.1.1(24) > 6.1.0(23) > 6.0.2(22) > 6.0.1(21) > 6.0.0(20) > 5.1.1(19) > 5.1.0(18) > 5.0.5(17)

在应用开发过程中，会依赖大量的三方库，应用hap和三方库har之间因为SDK版本属性字段的版本差异，会存在各种兼容性问题。

针对三方库本身的开发，建议开发者使用最新的编译的SDK版本，并且通过API兼容性判断机制，将运行的最低SDK版本配置为尽可能低（尤其是针对不依赖HarmonyOS SDK中API的三方库，建议将compatibleSdkVersion配置为12），这样能够满足尽可能多的应用集成，但可能需增加较多API兼容性判断保护，因此开发者需根据现网设备API版本占比情况综合评估后，有选择的进行设置。

| sdk属性 | 应用集成方关注点 | 三方库提供方关注点 | 应用集成三方库的规则 |
| --- | --- | --- | --- |
| compileSdkVersion | 1. 应用使用最新Release版本SDK进行开发；  2. 选择稳定且性能好的三方库版本进行集成； | 1. 不依赖系统API的三方库，该值建议设置为最新的Release的API版本；  2. 依赖系统API的三方库，该值建议设置为最新的Release的API版本。该值决定了可调用的API范围，如果需兼容运行到低版本，则需要对高版本的API进行兼容性判断保护。 | 1. 针对源码格式三方库，要求应用配置的compileSdkVersion版本≥三方库配置的compileSdkVersion版本，否则应用集成三方库编译时会报错；  2. 针对字节码格式三方库，无要求。 |
| targetSdkVersion | 1. 应用根据实际情况配置targetSdkVersion字段，从6.0.0(20)版本开始打开IDE时候，会提醒开发者配置该字段；  2. 应用升级该字段需要关注版本升级前后涉及到的API版本行为变更，需要进行适配；  3. 应用集成三方库时，需要关注和三方库targetSdkVersion值的差异。 | 1. 不依赖系统API的三方库，该值建议设置为最新的Release的API版本；  2. 依赖系统API的三方库：  （1）不存在行为变更API，则该值建议设置为最新的Release的API版本；  （2）存在行为变更API，则该值建议设置为最新的Release的API版本，并且需将使用的行为变更API全部都适配好，为应用集成方屏蔽差异。 | 1. 三方库中配置的targetSdkVersion版本和应用中配置的版本不同，则最终打包后会以应用中配置的targetSdkVersion版本为准；  2. 如果应用配置的targetSdkVersion版本和三方库配置的targetSdkVersion版本不一致，则需要关注三方库中targetSdkVersion版本变化是否会有API行为变更，从而进行相应适配（推荐由三方库统一屏蔽API行为差异；次选应用侧进行差异屏蔽）。 |
| compatibleSdkVersion | 1. 应用根据HarmonyOS系统现网API版本分布以及自身成本等情况选择合理值，建议支持至少95%以上的现网设备；  2. 应用集成三方库时，需要关注三方库该字段的值，并且关注三方库是否对高版本的API进行兼容性判断保护。 | 1. 不依赖系统API的三方库，该值可设置为5.0.0(12)，任意应用都可集成;  2. 依赖系统API的三方库，如果想被尽可能多的应用集成，则该值建议设置为≥近两年内最小的API版本。 | 1. 要求应用配置的compatibleSdkVersion版本≥三方库配置的compatibleSdkVersion版本，否则编译构建会报错。 |

为被targetSdkVersion值不同的宿主应用集成且三方库行为保持一致，三方库的提供方需在开发过程中，针对不同版本的API行为变更，通过调用getBundleInfoForSelf接口获取到宿主应用的bundleinfo.targetversion信息，从而对这些API行为进行适配处理。

**【示例1：应用集成三方库（含行为变更API）】**

（1）应用A的targetSdkVersion配置为5.0.1(13); 应用B的targetSdkVersion配置为5.0.2(14)；

（2）三方库的targetSdkVersion配置为5.0.2(14)， 且使用了@ohos.display.d.ts文件中屏幕Display对象的orientation属性，而该属性在5.0.2(14)版本进行了行为变更，系统侧为了不影响已上架应用，对该API行为进行了版本隔离。

（3）因为在应用集成三方库的时候，最终打包到应用中的targetSdkVersion字段值会填写为应用的值，则为了让三方库被应用集成后的行为一致，需要进行一些适配。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/cjCHej7UTfqAak148D-vkQ/zh-cn_image_0000002409845612.png "点击放大")

```screen
import bundleManager from '@ohos.bundle.bundleManager';
import display from '@ohos.display';
import hilog from '@ohos.hilog';
import deviceInfo from '@ohos.deviceInfo';
const TAG = 'DisplayCompat';
const SDK_VER_14 = 14;
const COMP_ID = 0xFF00;
enum Orientation {
  PORTRAIT = 0,
  LANDSCAPE = 1,
  PORTRAIT_INVERTED = 2,
  LANDSCAPE_INVERTED = 3
}
class DisplayCompat {
  private static targetVer = 0;
  private static deviceVer: number;
  private static callback: Callback<number>|null;
  public static async init() {
    if (!DisplayCompat.targetVer) {
      try {
        let bundleInfo:bundleManager.BundleInfo = await bundleManager.getBundleInfoForSelf(
          bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION
        );
        const targetSdkVersion = bundleInfo.targetVersion;
        DisplayCompat.targetVer = targetSdkVersion;
      } catch (e) {
        hilog.error(COMP_ID, TAG, 'Init failed: %{public}s', e);
      }
    }
    if (!DisplayCompat.deviceVer) {
      DisplayCompat.deviceVer = deviceInfo.sdkApiVersion;
    }
  }
  public static register(cb: Callback<number>) {
    if (typeof cb !== 'function') return;
    DisplayCompat.callback = cb;
    display.on('change', DisplayCompat.handleRotation);
  }
  public static unregister() {
    display.off('change', DisplayCompat.handleRotation);
    DisplayCompat.callback = null;
  }
  private static handleRotation = async (rot: number) => {
    if (!DisplayCompat.callback) return;
    try {
      if (!DisplayCompat.targetVer || !DisplayCompat.deviceVer) await DisplayCompat.init();
      const disp = display.getDefaultDisplaySync();
      if (!disp) return;
      // 判断是否使用旧版行为逻辑
      console.info(`mast shouldConvert()`+this.shouldConvert())
      DisplayCompat.callback(this.shouldConvert() ?
        this.convertOrientation(disp.orientation) : disp.rotation);
    } catch (e) {
      hilog.error(COMP_ID, TAG, 'Rotation error: %{public}s', e);
    }
  }
  /**
   * 判断是否使用旧版行为
   */
  private static shouldConvert() {
    // 目标版本<14 或 目标版本≥14但设备版本<14
    return DisplayCompat.targetVer % 100 < SDK_VER_14 ||
      (DisplayCompat.targetVer % 100 >= SDK_VER_14 && DisplayCompat.deviceVer < SDK_VER_14);
  }
  /**
   * 转换到旧版方向值
   * @param orientation 原始方向值
   */
  private static convertOrientation(orientation: number): number {
    // 设备在旧版本上的特殊处理
    switch (orientation) {
      case Orientation.LANDSCAPE:
        return Orientation.LANDSCAPE_INVERTED;
      case Orientation.LANDSCAPE_INVERTED:
        return Orientation.LANDSCAPE;
      default:
        return orientation;
    }
  }
}
export default DisplayCompat;
```

**【示例2: 应用集成三方库（具有更高compatibleSdkVersion版本】**

应用配置compatibleSdkVersion为5.0.0(12)，三方库配置的compatibleSdkVersion为5.0.1(13)， 当应用依赖这个三方库，编译构建时提示如下：

```screen
> hvigor ERROR: Failed :entry:default@MergeProfile...
> hvigor ERROR: 00306004 Specification Limit Violation
Error Message: The compatibleSDKVersion 12 cannot be smaller than 13 declared in library har.
```
