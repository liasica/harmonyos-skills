---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/package-structure-faq-0010
title: HAP/HAR/HSP包常见问题
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 常见问题 > HAP/HAR/HSP包常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:45+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:ca6b4017c07eed3088351cd6d7f57bd5f9bac77cbf64c5c88bd1672e652367cf
---

**Q：如何正确引用HAR/HSP包模块？**

**A**：在HarmonyOS应用开发中，处理包（HAR/HSP）模块间的依赖很常见。正确的依赖处理方式能确保代码模块化和可维护性，同时减少团队开发中的管理与沟通成本。以下是如何引用包模块的推荐和不推荐做法。

* 推荐方式：

  ```ts
    import \{ add \} from "library";
  ```
* 不推荐方式：

  不推荐使用相对路径或绝对路径进行引用。这种做法会破坏模块间的隔离性，增加团队开发的管理和沟通成本，且难以维护。例如：

  ```ts
    import \{ add \} from "../../library/src/main/ets/page/Index";
  ```

总结来说，为了保持代码的模块化、提高可维护性以及降低团队协作的复杂度，推荐使用包名进行模块间的依赖引用。避免使用相对或绝对路径，以维护项目的结构清晰和高效的团队合作。更多请参见[HAR](../harmonyos-guides/har-package.md)。

**Q：在项目中经常会接触到HAR、HSP、HAP，这三者有什么区别，它们的使用场景分别是什么？**

**A**：

| 对比维度 | HAP | HAR | HSP |
| --- | --- | --- | --- |
| 定义 | 应用安装和运行的基本单元，包含代码、资源、配置等，  分 entry（主模块，必须存在）和 feature（动态特性模块，可选） | 静态共享包，用于复用代码/资源（如UI组件、工具类） | 动态共享包，运行时被多个模块共享 |
| 跨应用共享 | 不可共享 | 可发布至OHPM中心仓/私仓 | 仅限应用内共享 |
| 资源复用方式 | 不涉及 | 编译时复制到引用模块 | 运行时动态加载 |
| 多模块引用影响 | 不涉及 | 代码/资源重复拷贝 → 包体积增大 | 仅保留一份→ 节省空间 |
| 典型使用场景 | 1、主入口模块：实现应用启动页、核心功能；  2、动态特性模块：可选扩展功能（如视频播放、支付模块），支持动态部署（按需下载安装）。 | 1、公共UI组件库、工具类封装；  2、跨团队/企业共享：发布至OHPM中心仓或私仓供其他应用调用。 | 1、多模块共用大资源（如图片、视频），避免重复打包、拷贝；  2、元服务分包预加载，提升性能；  3、解决HAR导致的包膨胀问题。 |
| 调试打包 | 调试时需生成.hap文件，通过DevEco Studio或命令行直接安装到设备。 | 直接打包到HAP中，调试时无需单独安装。 | 避免重复拷贝，需与宿主HAP同进程运行，测试时需先安装HSP再装HAP。 |
| 关键限制 | 1、不支持声明Ability/Page，但可通过Navigation跳转包含的页面；  2、禁止循环依赖，不能引用AppScope资源。 | 1、需与宿主HAP版本号严格一致；  2、不能独立发布到应用市场。 | 不可作为共享包给其他应用使用。 |

**Q：多模块使用同一个HAR，APP中会有多个HAR包还是只有一个？**

**A**：会存在多份。每个使用方都会拷贝一份HAR到对应模块，造成包体积增大，如果是重复资源等大体积文件，建议使用HSP替换。

**Q：在HAR包中是否可以创建AbilityStage，该AbilityStage的生命周期什么时候执行？**

**A**：不能。AbilityStage与HAP包一一对应。具体关系可见下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/oHkOL-APT_GNg8fQid1H3g/zh-cn_image_0000002803284281.png "点击放大")

**Q：HAR转HSP后，编译报错，该怎么排查？**

**A**：[HAR转HSP包转换后](../harmonyos-guides/har-to-hsp.md#har转hsp的操作步骤)，需确保以下配置正确：

* 检查HAR下的module.json5中，是否设置"type": "shared"，并添加"deliveryWithInstall"。
* 检查module中hvigorfile.ts文件，是否将harTasks改为了hspTasks。
* HAR包的build-profile.json5默认会有"consumerFiles": './consumer-rules.txt' ，该项仅HAR模块可配置，为默认导出的混淆规则，需将其删除。

**Q：多HSP引用同一个HAR，在A HSP中已经初始化过HAR中的值，在B HSP中使用的时候HAR中的值还是默认值，请问如何解决？**

**A**：HAR被多个HSP引用后，会被拷贝多份至每个HSP中，所以不能多个模块共享一个HAR中实例。如涉及此场景建议用HSP替代HAR。

**Q：什么场景下会用到多个HAP？**

**A**：多个HAP主要是方便开发者模块化的管理应用，方便开发者将多HAP合理地组合并部署到不同的设备上，按需加载，减少包大小。例如支付类应用，有统一的主界面，主界面管理“扫一扫”、“收付款”、“消息”、“理财”等各个模块。其中主界面管理其他模块的逻辑在entry包中实现，而“扫一扫”、“收付款”、“消息”和“理财”等模块在不同的feature包中实现。可以同时开发多个feature包，能够实现feature包单独的开发测试，最终由entry包统一集成feature包的特性。

**Q：HAP能作为共享包给其它应用使用吗？**

**A**：不能，作为共享包给其它应用使用请使用HAR或集成态HSP。

**Q：HSP怎么上传中心仓给其它三方应用使用？**

**A**：OpenHarmony三方库中心仓仅支持HAR共享包发布，不支持HSP共享包发布。如需在应用内共享HSP，可将HSP共享包发布至私仓使用，请参考[ohpm私仓搭建工具](../harmonyos-guides/ide-ohpm-repo-overview.md)。

**Q：项目中有一个entry类型的module，多个feature类型的module，如何在程序启动后指定加载feature类型的module？**

**A**：程序启动入口module只能是entry类型，无法启动指定加载feature类型的module，但是各个module的类型可以在“entry”和“feature”之间随意指定，只要保证只有一个entry类型的module即可，程序启动就会加载这个module，可以在module的module.json5文件中修改[type属性](../harmonyos-guides/module-configuration-file.md#配置文件标签)。

**Q：应用内共享HSP编译成.tgz包如何依赖外部的HAR包？**

**A**：需要将依赖的HAR包内置于HSP包中一同编译成.tgz格式。

**Q：应用内共享HSP编译成.tgz包如何依赖外部的HSP包？**

**A**：需要将依赖的HSP包内置于HSP包中一同编译成.tgz格式或将依赖的HSP发布到私仓在共享HSP开发过程中通过版本号进行依赖。

**Q：HAP可以设置为单独的进程吗？**

**A**：在2in1和tablet设备上，针对UIAbility支持将HAP设置为独立进程，[模块独立进程](../harmonyos-guides/process-model-stage.md)。

**Q：发布到应用市场APP包为什么会比HAP包小？**

**A**：APP里编译的HAP包一般会比正常编译的HAP包小，编译APP包默认是非Debug模式，编译HAP包默认Debug模式，Debug版本相对于release版本包含了完整的调试信息和符号表，这些信息可以帮助开发者在调试过程中快速定位问题，查看变量值、函数调用栈等。此外，Debug版本没有进行混淆和优化导致包体积也会相对于release版本更大。

**Q：安装时是先安装的HSP再安装的HAP。如果后续HAP有更新，是可以直接hdc install hap么？如果卸载HAP，相关依赖的HSP也会卸载吗？**

**A**：直接hdc install xxx.hap即可，不需要卸载重装；不会卸载HSP，HSP是共享模块，可能被多个HAP共用。

**Q：工程级oh-package.json中依赖A HAR模块，编译后A HAR会被打入B HSP中，实际B HSP并未依赖A HAR，且运行提示A、B循环依赖？**

**A**：工程级oh-package.json中声明的依赖是整个项目的，会被所有模块依赖，当前不建议在工程级依赖中配置非devDependencies的依赖，即一个Hsp/Har模块的非开发态依赖都要在相应模块的dependencies和dynamicDependencies中声明。将工程级oh-package.json中声明的依赖在各自需要的模块的oh-package.json中按需声明即可。

**Q：HAP依赖HSP、HAR，HSP不依赖HAR时，HSP可以使用HAR中资源吗？**

**A**：HSP和HAR二者不存在依赖关系，HSP是不能使用HAR中资源的。

**Q：在应用开发测试过程中，APP格式的包打出来没法给测试安装吗？**

**A**：APP是应用市场发布格式（类似APK），包含所有HAP/HSP的压缩包，但设备无法直接安装，仅用于上架。调试阶段需将APP包拆分为散包（HAP/HSP），通过hdc工具或IDE安装，便于单模块更新。

**Q：HAP/HAR/HSP是否都可以声明注册Ability和page？**

**A**：HAP/HAR/HSP均支持在配置文件中声明abilities、extensionAbilities组件，HAP/HSP支持在配置文件中声明page页面。

**Q：如何理解App、HAP、HAR、HSP的关系？**

**A**：App、HAP、HAR、HSP的关系如下：

* App是发布到应用市场的基本单元，不能直接在设备上安装和运行。
* HAP（Harmony Ability Package）是应用安装和运行的基本单元，包含代码、资源、第三方库及配置文件等，主要分为entry和feature两种类型。
* HAR（Harmony Archive）是静态共享包，包含代码、C++库、资源和配置文件。HAR支持多个模块或工程共享ArkUI组件和相关代码。
* HSP（Harmony Shared Package）是动态共享包，包含代码、C++库、资源和配置文件，用于实现代码和资源的共享。HSP跟随宿主应用的App包一起发布，与宿主应用同进程，具有相同的包名和生命周期。

**Q：调试报错“Error message:cannot find record '&XXX/src/main/ets/YYY&x.y.z', please check the request path.'ZZZ.abc'.”，如何解决？**

**A**：在使用DevEco Studio推包到设备进行调试时，如果遇到jscrash报错，FaultLog中显示“Error message: cannot find record '&XXX/src/main/ets/YYY&x.y.z'，请检查请求路径 'ZZZ.abc'”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/OzTQZqfrTn6sk9o7D-cknQ/zh-cn_image_0000002773924892.png "点击放大")

问题原因及解决措施如下：

场景一：字节码HAR（H）使用的依赖包XXX未配置在本模块的oh-package.json5的dependencies或dynamicDependencies中（错误地配置在了工程级oh-package.json5中），请参考[字节码HAR约束条件](../harmonyos-guides/ide-hvigor-build-har.md#section38518561610)。

解决措施：需要字节码HAR（H）的生产方重新出包，将对XXX包的依赖添加到本模块的oh-package.json5中。

场景二：用户在工程级oh-package.json5和模块级oh-package.json5中同时依赖了XXX包的不同版本，请参考[字节码HAR约束条件](../harmonyos-guides/ide-hvigor-build-har.md#section38518561610)。

解决措施：

措施1：手工修改工程级或模块级oh-package.json5，将XXX的版本调整一致。

措施2：通过工程级oh-package.json5中的overrides字段，覆盖模块中使用的其他版本。

场景三：将HSP包转成HAR包后，未删除"packageType"，导致按字节码进行打包的时候未解析其相关依赖，请参考[HSP转HAR指导](../harmonyos-guides/hsp-to-har.md#hsp转har的操作步骤)。

解决措施：参考"HSP转HAR指导"中的第四步，将模块的oh-package.json5文件中"packageType": "InterfaceHar" 配置删除。

场景四：使用了不兼容的第三方插件或SDK对代码进行了修改（如混淆、加固类的SDK），导致了代码无法识别。

解决措施：联系对应三方插件或SDK进行解决，如升级版本。

场景五：应用依赖了包XXX，该XXX包在构建时使用了[增量构建](../harmonyos-guides/ide-hvigor-incremental-build.md)的方式，且同时修改了模块级oh-package.json5中的version字段，导致了XXX包中部分文件在寻址时还是用老的版本号去寻址，进而导致找不到相关文件。

解决措施：

措施1：在XXX包对应工程中执行Build > Clean Project操作，然后重新构建项目。

措施2：在工程级hvigorfile.ts文件中增加插件来修复。

1. 在工程根目录下新增plugin.ts文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/UUFhH0UKTJO2mHeG2XZJ6A/zh-cn_image_0000002803284691.png "点击放大")

   plugin.ts文件内容：

   ```ts
   import {OhosPluginId, Target} from '@ohos/hvigor-ohos-plugin';
   import {hvigor, HvigorNode, HvigorPlugin} from '@ohos/hvigor';
   import path from "path";
   import fs from "fs";

   function getLoaderJsonPath(target: Target) {
     return path.resolve(target.getBuildTargetOutputPath(), `../../intermediates/loader/${target.getTargetName()}/loader.json`);
   }

   function getPkgContextInfoPath(target: Target) {
     return path.resolve(target.getBuildTargetOutputPath(), `../../intermediates/loader/${target.getTargetName()}/pkgContextInfo.json`);
   }

   function deleteLoaderJson(target: Target) {
     const loaderJsonPath = getLoaderJsonPath(target);
     if (fs.existsSync(loaderJsonPath)) {
       fs.rmSync(loaderJsonPath);
     }
   }

   function deletePkgContextInfo(target: Target) {
     const pkgContextInfoPath = getPkgContextInfoPath(target);
     if (fs.existsSync(pkgContextInfoPath)) {
       fs.rmSync(pkgContextInfoPath);
     }
   }

   function deleteRollupCache(target: Target, buildMode: string) {
     const arkTSCompileCachePath = path.resolve(target.getBuildTargetOutputPath(),
       `../../cache/${target.getTargetName()}/${target.getTargetName()}@HarCompileArkTS/esmodule/${buildMode}/compiler.cache`);
     if (fs.existsSync(arkTSCompileCachePath)) {
       fs.rmSync(arkTSCompileCachePath, { recursive: true });
     }
   }

   function updateHapHspAbcVersion(subNode: HvigorNode, target: Target) {
     const task = subNode.getTaskByName(`${target.getTargetName()}@GenerateLoaderJson`);
     if (!task) {
       console.log('GenerateLoaderJson not found.');
       return;
     }
     deleteLoaderJson(target);
     deletePkgContextInfo(target);
     task.afterRun(() => {
       const pkgContextInfoPath = getPkgContextInfoPath(target);
       if (!fs.existsSync(pkgContextInfoPath)) {
         console.log('pkgContextInfo not found.');
         return;
       }
       const pkgContextInfoObj = JSON.parse(fs.readFileSync(pkgContextInfoPath).toString());
       if (!pkgContextInfoObj) {
         console.log('pkgContextInfo parse failed.');
         return;
       }
       const loaderJsonPath = getLoaderJsonPath(target);
       if (!fs.existsSync(loaderJsonPath)) {
         console.log('loaderJson not found.');
         return;
       }
       const loaderJsonObj = JSON.parse(fs.readFileSync(loaderJsonPath).toString());
       if (!loaderJsonObj) {
         console.log('loaderJson parse failed.');
         return;
       }
       for (const [key, value] of Object.entries(pkgContextInfoObj)) {
         if (!value?.version) {
           continue;
         }
         if (!loaderJsonObj.updateVersionInfo[key]) {
           loaderJsonObj.updateVersionInfo[key] = {};
         }
         loaderJsonObj.updateVersionInfo[key][key] = value.version;
       }
       fs.writeFileSync(loaderJsonPath, JSON.stringify(loaderJsonObj));
     });
   }

   function updateHarAbcVersion(target: Target) {
     deleteLoaderJson(target);
     deleteRollupCache(target, 'debug');
     deleteRollupCache(target, 'release');
   }

   // The user of bytecode har can use this plugin to correctly modify the version number of ohmurl in abc when integrating bytecode har, ensuring no crashes during runtime
   export function updateAbcVersionPlugin(): HvigorPlugin {
     return {
       pluginId: 'updateAbcVersionPlugin',
       apply(node: HvigorNode) {
         hvigor.nodesEvaluated(() => {
           hvigor.getRootNode().subNodes(subNode => {
             let context = subNode.getContext(OhosPluginId.OHOS_HAP_PLUGIN);
             if (!context) {
               context = subNode.getContext(OhosPluginId.OHOS_HSP_PLUGIN);
             }
             if (!context) {
               return;
             }
             context.targets(target => {
               updateHapHspAbcVersion(subNode, target);
             });
           });
         });
       }
     };
   }

   // The generator of bytecode har uses this plugin to incrementally build ohmurl with the correct bytecode har after modifying the version number
   export function updateHarAbcVersionPlugin(): HvigorPlugin {
     return {
       pluginId: 'updateHarAbcVersionPlugin',
       apply(node: HvigorNode) {
         hvigor.nodesEvaluated(() => {
           hvigor.getRootNode().subNodes(subNode => {
             const context = subNode.getContext(OhosPluginId.OHOS_HAR_PLUGIN);
             if (!context) {
               return;
             }
             context.targets(target => {
               updateHarAbcVersion(target);
             });
           });
         });
       }
     };
   }
   ```
2. 在工程级hvigorfile.ts文件中增加两个插件，并执行Sync。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/ZzgrR5VFRpecOI3GG-0Q8A/zh-cn_image_0000002773925252.png "点击放大")

   hvigorfile.ts文件内容：

   ```ts
   import { appTasks } from '@ohos/hvigor-ohos-plugin';
   import { updateAbcVersionPlugin, updateHarAbcVersionPlugin } from './plugin.ts';

   export default {
       system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
       plugins:[updateAbcVersionPlugin(), updateHarAbcVersionPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
   }
   ```
3. 在Terminal终端执行以下命令后，重新推包运行。

   ```shell
   hvigorw --stop-daemon
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/i3Xui2T3SoaV_NY0nIPuUw/zh-cn_image_0000002803245341.png "点击放大")
