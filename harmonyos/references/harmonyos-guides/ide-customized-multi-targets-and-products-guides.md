---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-customized-multi-targets-and-products-guides
title: 能力说明
breadcrumb: 指南 > 构建应用 > 配置构建流程 > 配置多目标产物 > 能力说明
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:21+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:4f57379f0e4c5fe0b7f45a53e46fbc0d6a211036fade1e650e1b039195b95bd9
---

通常情况下，应用厂商会根据不同的部署环境，不同的目标人群，不同的运行环境等，将同一个应用定制为不同的版本，如国内版、国际版、普通版、VIP版、免费版、付费版等。针对以上场景，DevEco Studio支持通过少量的代码配置以实例化不同的差异版本，在编译构建过程中实现一个应用构建出不同的目标产物版本，从而实现源代码、资源文件等的高效复用。

在了解HarmonyOS应用的多目标构建产物如何定制前，先了解target和product的概念：

* 工程内的每一个Entry/Feature模块，对应的构建产物为HAP，HAP是应用/元服务可以独立运行在设备中的形态。由于在不同的业务场景中，同一个模块可能需要定制不同的功能或资源，因此引入target的概念。一个模块可以定义多个target，每个target对应一个定制的HAP，通过配置可以实现一个模块构建出不同的HAP。
* 一个HarmonyOS工程的构建产物为APP包，APP包用于应用/元服务发布上架应用市场。由于不同的业务场景，需要定制不同的应用包，因此引入product概念。一个工程可以定义多个product，每个product对应一个定制化应用包，通过配置可以实现一个工程构建出多个不同的应用包。

更多关于多目标产物的实践请参考[多目标产物构建开发实践](../best-practices/bpta-multi-target.md)。

## 定制HAP多目标构建产物

每一个Entry/Feature模块均支持定制不同的target，通过在模块中的build-profile.json5文件中实现差异化定制，当前支持HAP包名、设备类型（deviceType）、源码集（source）、资源（resource）、buildOption配置项（如C++依赖的.so、混淆配置、abi类型、cppFlags等）、分发规则（distributionFilter）的定制。

**定义目标产物target**

每一个target对应一个定制的HAP，因此，在定制HAP多目标构建产物前，应提前规划好需要定制的target名称。例如，以ArkTS Stage模型为例，定义一个免费版和付费版，模块级build-profile.json5文件示例如下：

```json5
{ 
  "apiType": 'stageMode', 
  "buildOption": {   
  }, 
  "targets": [  //定义不同的target 
    { 
      "name": "default",  //默认target名称default 
    }, 
    { 
      "name": "free",  //免费版target名称 
    }, 
    { 
      "name": "pay",  //付费版target名称 
    } 
  ] 
}
```

按照上述target的定义，在编译构建时，会同时打包生成default、free和pay三个不同的HAP。

### 定义产物的HAP包名

每一个target均可以指定产物命名。

```json5
{ 
  "apiType": "stageMode", 
  "buildOption": { 
  }, 
  "targets": [ 
    { 
      "name": "default", 
      "output": { 
        "artifactName": "customizedTargetOutputName-1.0.0"  //产物名称为customizedTargetOutputName-1.0.0
      } 
    }, 
    { 
      "name": "free", 
      "output": { 
        "artifactName": "customizedTargetOutputName1-1.0.0"  //产物名称为customizedTargetOutputName1-1.0.0
      } 
    }, 
    { 
      "name": "pay", 
      "output": { 
        "artifactName": "customizedTargetOutputName2-1.0.0"  //产物名称为customizedTargetOutputName2-1.0.0
      } 
    } 
  ] 
}
```

如果已配置签名，target产物对应的HAP包名为开发者定制的名称；如果未配置签名，target产物对应的HAP包名为开发者定制的名称+unsigned。

### 定义产物的deviceType

每一个target均可以指定支持的设备类型deviceType，也可以不定义。如果不定义，则该target默认支持module.json5（Stage模型）/config.json（FA模型）中定义的设备类型。

同时，在定义每个target的deviceType时，支持的设备类型必须在module.json5或config.json中已经定义。例如，在上述定义的3个target中，分别定义default默认支持所有设备类型，free和pay版本只支持phone设备。

```json5
{ 
  "apiType": 'stageMode', 
  "buildOption": { 
  }, 
  "targets": [ 
    { 
      "name": "default",  //未定义deviceType，默认支持config.json或module.json5中定义的设备类型 

    }, 
    { 
      "name": "free", 
      "config": { 
        "deviceType": [  //定义free支持的设备类型为phone 
          "phone" 
        ] 
      } 
    }, 
    { 
      "name": "pay", 
      "config": { 
        "deviceType": [  //定义pay支持的设备类型为phone 
          "phone" 
        ] 
      } 
    } 
  ] 
}
```

### 定义产物的distributionFilter

在未定义target的分发规则distributionFilter时，以module配置[distributionFilter](module-configuration-file.md#distributionfilter标签)/[distroFilter](../lite-wearable-guides/module-structure.md#distrofilter对象的内部结构)分发规则为准。

针对多target存在相同设备类型deviceType的场景，相同设备类型的target需要指定分发规则distributionFilter。

如果是FA工程，请将distributionFilter字段替换为distroFilter。

```json5
{ 
  "apiType": "stageMode", 
  "buildOption": { 
  }, 
  "targets": [ 
    { 
      "name": "default", 

    }, 
    { 
      "name": "free", 
      "config": { 
        "distributionFilter": {  // 具体请参考distributionFilter标签
          "screenShape": { // 屏幕形状枚举 
            "policy": "include", 
            "value": ["circle"] 
          } 
        } 
      } 
    }, 
    { 
      "name": "pay", 
      "config": { 
        "distributionFilter": { 
          "screenShape": { 
            "policy": "include", 
            "value": ["rect"] 
          } 
        } 
      } 
    } 
  ] 
}
```

### 定义产物preloads的分包

对于元服务，每一个target均可以指定preloads的分包，也可以不定义。如果不定义，则以module.json5中的配置为准。

```json5
{ 
  "apiType": 'stageMode', 
  "showInServiceCenter": true, 
  "buildOption": { 
  }, 
  "targets": [   
    { 
      "name": "default",   
    },
    { 
      "name": "free",   
    },
    { 
      "name": "pay",   
      "config": { 
        "atomicService": { 
          "preloads": [  //指定preloads的分包 
            { 
              "moduleName": "preloadSharedLibrary"
            } 
          ] 
        } 
      } 
    } 
  ] 
}
```

### 定义产物的source源码集-pages

对于source源码集的定制，由于Stage模型和FA模型的差异，Stage模型支持对pages源码目录的page页面进行定制，FA模型则支持对Ability源码目录下的page页面进行定制。

* 例如，Stage模型中的工程，在模块的pages目录下分别定义了Index.ets、Page1.ets和Page2.ets三个页面。其中default使用了Index.ets页面；free使用了Index.ets和Page1.ets页面；pay使用了Index.ets和Page2.ets页面，则示例代码如下所示：

  ```json5
  { 
     "apiType": 'stageMode', 
     "buildOption": { 
     }, 
     "targets": [ 
       { 
         "name": "default", 
         "source": {  //定义Stage模型中默认版target的pages源码文件
           "pages": [ 
             "pages/Index" 
           ] 
         } 
       }, 
       { 
         "name": "free", 
         "config": { 
           "deviceType": [ 
             "phone" 
           ] 
         }, 
         "source": {  //定义Stage模型中免费版target的pages源码文件
           "pages": [ 
             "pages/Index", 
             "pages/Page1" 
           ] 
         } 
       }, 
       { 
         "name": "pay", 
         "config": { 
           "deviceType": [ 
             "phone" 
           ] 
         }, 
         "source": {  //定义Stage模型中付费版target的pages源码文件
           "pages": [ 
             "pages/Index", 
             "pages/Page2" 
           ] 
         } 
       } 
     ] 
   }
  ```

* 例如，FA模型中的工程，在模块的MainAbility中定义了index.ets、page1.ets和page2.ets，其中：default使用了index.ets 页面；free使用了index.ets和page1.ets页面；pay使用了index.ets和page2.ets页面。

  ```json5
  { 
     "apiType": 'faMode', 
     "buildOption": { 
     }, 
     "targets": [ 
       { 
         "name": "default", 
         "source": {  //定义FA模型中默认版target的pages源码文件
           "abilities": [ 
             { 
               "name": ".MainAbility", 
               "pages": [ 
                 "pages/index" 
               ] 
             } 
           ], 
         } 
       }, 
       { 
         "name": "free", 
         "config": { 
           "deviceType": [ 
             "phone" 
           ] 
         }, 
         "source": {  //定义FA模型中免费版target的pages源码文件
           "abilities": [ 
             { 
               "name": ".MainAbility", 
               "pages": [ 
                 "pages/index", 
                 "pages/page1" 
               ] 
             } 
           ], 
         } 
       }, 
       { 
         "name": "pay", 
         "config": { 
           "deviceType": [ 
             "phone" 
           ] 
         }, 
         "source": {  //定义FA模型中付费版target的pages源码文件
           "abilities": [ 
             { 
               "name": ".MainAbility", 
               "pages": [ 
                 "pages/index", 
                 "pages/page2" 
               ] 
             } 
           ], 
         } 
       } 
     ] 
   }
  ```

### 定义产物的source源码集-sourceRoots

在模块的主代码空间（src/main）下，承载着开发者编写的公共代码。如果开发者需要实现不同target之间的差异化逻辑，可以使用差异化代码空间（sourceRoots）。配合差异化代码空间的能力，可以在主代码空间中代码不变的情况下，针对不同的target，编译对应的代码到最终产物中。

**概念说明**

* packageName：当前模块的oh-package.json5中的name字段对应的值。
* sourceRoots：<defaultSourceRoot> | <targetSourceRoot> ，其中<defaultSourceRoot>是 src/main，<targetSourceRoot>可自定义，寻址优先级为 <targetSourceRoot> > <defaultSourceRoot>。
* sourcePath：在sourceRoots中的代码结构目录。
* sourceFileName：代码目录下的ets文件名。

例如以下工程目录：

```json
entry
|--src
|----main
|------ets
|--------code
|----------test.ets
|----target
|------util
|--------util.ets
```

* packageName为entry。
* sourceRoots为src/main、src/target。
* sourcePath为ets/code、util。
* sourceFileName为test.ets、util.ets。

**规格限制**

1. import xxx from '<packageName>/sourcePath/sourceFileName' ：通过packageName的方式，省略sourceRoots，可以实现不同target下的差异化构建。
2. sourceRoots只能配置到src的下一级目录，如src/main，不支持多级子目录。
3. 支持hap、hsp、har（请注意：开启[文件/文件夹名称混淆](source-obfuscation-rule-options.md#section-enable-filename-obfuscation)的har模块需要使用-keep-file-name指定sourceRoots，sourcePath，sourceFileName对应的文件/文件夹名称不被混淆）。
4. 不支持跨模块引用。
5. 不支持动态import。

**编译时模块target的选择优先级说明**

在模块编译的过程中，该模块使用的sourceRoots由当前模块编译时的target来决定。当前模块编译时选择target的优先级则为：命令行显式指定 > 直接引用方target > default。

如以下示例：

hap -> hsp -> har（->表示依赖）

其中hap和hsp存在三个target：default、custom、static，而har存在两个target：default、static。

* 执行编译命令：hvigorw -p module=hap@custom assembleHap，hap指定target为custom进行编译，那么三个模块编译时的target分别为：

  hap: custom，命令行显式指定；

  hsp: custom，命令行没有显式指定，则基于直接引用方查找，hsp的直接引用方为hap，hap的target为custom，hsp存在该target，则hsp的target为custom；

  har: default，命令行没有显式指定，则基于直接引用方查找，har的直接引用方为hsp，hsp的target为custom，har不存在该target，则har的target为default；

* 执行编译命令：hvigorw -p module=hap@custom,hsp@static assembleHap assembleHsp，hap指定target为custom，hsp则指定target为static进行编译，那么三个模块编译时的target分别为：

  hap: custom，命令行显式指定；

  hsp: static，命令行显式指定；

  har: static，命令行没有显式指定，则基于直接引用方查找，har的直接引用方为hsp，hsp的target为static，har存在该target，则har的target为static。
* 在当前依赖关系的基础上，添加依赖：hap -> har。执行编译命令：hvigorw -p module=hap@custom,hsp@static assembleHap assembleHsp。由于har没有显式指定target，且存在两个target不同的直接引用方（hap和hsp，对应的target分别为custom和static），所以编译过程中har的target只能二选一。基于这种场景，建议开发者显式指定模块的target进行编译：hvigorw -p module=hap@custom,hsp@static,har@static assembleHap assembleHsp assembleHar。

**示例**

1. 在entry模块的build-profile.json5中添加sourceRoots：

```json5
{
  "apiType": "stageMode",
  "buildOption": {},
  "targets": [ 
    { 
      "name": "default", 
      "source": { 
        "sourceRoots": ["./src/default"] // 配置target为default的差异化代码空间
      } 
    }, 
    { 
      "name": "custom", 
      "source": { 
        "sourceRoots": ["./src/custom"] // 配置target为custom的差异化代码空间
      } 
    } 
  ]
}
```

2. 在src目录下新增default/Test.ets和custom/Test.ets，新增后的模块目录结构：

```txt
entry
  |--src
    |--main
      |--ets
        |--pages
          |--Index.ets
    |--default
      |--Test.ets  // 新增
    |--custom
      |--Test.ets  // 新增
```

3. 在default/Test.ets中写入代码：

```ts
export const getName = () => "default"
```

4. 在custom/Test.ets中写入代码：

```ts
export const getName = () => "custom"
```

5. 修改src/main/ets/pages/Index.ets的代码：

```ts
import { getName } from 'entry/Test'; // 其中entry为模块级的oh-package.json5中的name字段的值
@Entry
@Component
struct Index { 
  @State message: string = getName(); 
  build() { 
    RelativeContainer() { 
      Text(this.message) 
    } 
    .height('100%') 
    .width('100%') 
  }
}
```

6. 在工程级的build-profile.json5中配置targets：

```json5
{
  "app": {
    "signingConfigs": [],
    "products": [
      {
        "name": "default",
        "signingConfig": "default",
        "compatibleSdkVersion": "26.0.0",
        "runtimeOS": "HarmonyOS",
      }
    ],
    "buildModeSet": [
      {
        "name": "debug",
      },
      {
        "name": "release"
      }
    ]
  },
  "modules": [
    {
      "name": "entry",
      "srcPath": "./entry",
      "targets": [
        {
          "name": "default",
          "applyToProducts": [
            "default"
          ]
        },
        {
          "name": "custom",
          "applyToProducts": [
            "default"
          ]
        }
      ]
    }
  ]
}
```

7. Sync完成后，选择entry的target为default，点击Run，界面展示default；选择entry的target为custom，点击Run，则界面展示custom。

### 定义产物的资源

每个target使用的资源文件可能存在差异，在开发过程中，开发者可以将每个target所使用的资源存放在不同的资源目录下。其中，ArkTS工程支持对main目录下的资源文件目录（resource）进行定制；JS工程支持对main目录下的资源文件目录（resource）及 Ability下的资源文件目录（res）进行定制。如下为ArkTS工程的资源文件目录定制示例：

```json5
{ 
  "apiType": 'stageMode', 
  "buildOption": { 
  }, 
  "targets": [ 
    { 
      "name": "default", 
      "source": { 
        "pages": [ 
          "pages/Index" 
        ] 
      }, 
      "resource": {  // 定义默认版target使用的资源文件目录 
        "directories": [ 
          "./src/main/resources_default" 
        ] 
      } 
    }, 
    { 
      "name": "free", 
      "config": { 
        "deviceType": [ 
          "phone" 
        ] 
      }, 
      "source": {   
        "pages": [ 
          "pages/Index", 
          "pages/Page1" 
        ] 
      }, 
      "resource": {  // 定义免费版target使用的资源文件目录 
        "directories": [ 
          "./src/main/resources_free",
          "./src/main/resources_default"
        ] 
      } 
    }, 
    { 
      "name": "pay", 
      "config": { 
        "deviceType": [ 
          "phone" 
        ] 
      }, 
      "source": {   
        "pages": [ 
          "pages/Index", 
          "pages/Page2" 
        ] 
      }, 
      "resource": {  // 定义付费版target使用的资源文件目录
        "directories": [ 
          "./src/main/resources_pay",
          "./src/main/resources_default"
        ] 
      } 
    } 
  ] 
}
```

编译构建时，资源文件存在以下优先级顺序：

* AppScope目录下的资源文件会合入到模块下相同路径的资源目录中。如果两个目录下存在重名文件，编译打包后AppScope目录下的资源文件会覆盖模块下的资源。
* 如果target引用的多个资源文件目录下，存在重名文件，则在构建打包过程中，将按照配置的资源文件目录顺序进行选择。例如，上述付费版target引用的资源中，resources\_pay和resources\_default中存在重名文件，则resources\_pay中的资源会被打包到HAP中。

### 定义产物的icon、label、launchType

针对每个target的ability，均可以定制不同的icon、label和launchType。如果不定义，则该target采用module.json5中module.abilities配置的icon、label，launchType默认为"singleton"。示例如下所示：

```json5
{ 
   "apiType": 'stageMode', 
   "buildOption": { 
   }, 
   "targets": [ 
     { 
       "name": "default", 
       "source": {
        "abilities": [
          {
            "name": "EntryAbility",
            "icon":"$media:layered_image",
            "label":"$string:EntryAbility_label",
            "launchType": "singleton"
          }
        ]
      }
     }, 
     { 
       "name": "free", 
       "source": {
        "abilities": [
          {
            "name": "EntryAbility",
            "icon":"$media:layered_image",
            "label":"$string:EntryAbility_label",
            "launchType": "multiton"
          }
        ]
      }
     }
   ] 
 }
```

### 定义C++工程依赖的.so文件

在 C++ 工程中，可以对每个target依赖的.so文件进行定制。例如某模块依赖了function1.so、function2.so和function3.so三个文件，其中target为default的产物依赖了function1.so和function2.so；其中target为vip的产物依赖了function1.so和 function3.so，则示例代码如下所示：

```json5
{
  "apiType": 'stageMode',
  "buildOption": {
    "externalNativeOptions": {
      "path": "./src/main/cpp/CMakeLists.txt",
      "arguments": [],
      "abiFilters": [
        "arm64-v8a",
        "x86_64"
      ],
      "cppFlags": "",
    }
  },
  "targets": [  //定义不同的target 
    {
      "name": "default",
      "config": {
        "buildOption": {
          "nativeLib": {
            "filter": {
              //按照.so文件的优先级顺序，打包最高优先级的function1.so文件 
              "pickFirsts": [
                "**/function1.so"
              ],
              //排除不打包的function3.so文件 
              "excludes": [
                "**/function3.so"
              ],
              //允许当.so中资源重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件 
              "enableOverride": true
            }
          }
        }
      }
    },
    {
      "name": "vip",
      "config": {
        "buildOption": {
          "nativeLib": {
            "filter": {
              //按照.so文件的优先级顺序，打包最高优先级的function1.so文件 
              "pickFirsts": [
                "**/function1.so"
              ],
              //排除不打包的function2.so文件 
              "excludes": [
                "**/function2.so"
              ],
              //允许当.so中资源重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件 
              "enableOverride": true
            }
          }
        }
      }
    }
  ]
}
```

## 定制HAR多目标构建产物

每一个HAR模块均支持定制不同的target，通过在模块中的build-profile.json5文件中实现差异化定制，当前支持设备类型（deviceType）、资源（resource）、buildOption配置项（如C++依赖的.so、混淆配置、abi类型、cppFlags等）、源码集（source）的定制。

DevEco Studio 6.0.2 Beta1版本之前，在DevEco Studio中构建HAR模块时，仅支持default target，若需指定其他target，需通过命令行来指定和构建。

例如构建自定义target为free的HAR，可参考执行以下命令：

```bash
hvigorw --mode module -p product=default -p module=library@free -p buildMode=debug assembleHar
```

从DevEco Studio 6.0.2 Beta1版本开始，支持在DevEco Studio中选择HAR模块的target，选择的target仅在单独构建HAR包时生效。如果是构建HAP/HSP，会动态计算依赖HAR的target，具体请参考[多产物构建target](ide-customized-multi-targets-and-products-guides.md#section7121513141619)。

### 定义产物的deviceType

每一个target均可以指定支持的设备类型deviceType，也可以不定义。如果不定义，则该target默认支持module.json5/[config.json](../lite-wearable-guides/application-configuration-file-overview-fa.md)中定义的设备类型。

同时，在定义每个target的deviceType时，支持的设备类型必须在module.json5或config.json中已经定义。例如，在上述定义的2个target中，分别定义default默认支持所有设备类型，free版本只支持2in1设备。

```json5
{ 
  "apiType": 'stageMode', 
  "buildOption": { 
  }, 
  "targets": [ 
    { 
      "name": "default"  //未定义deviceType，默认支持config.json或module.json5中定义的设备类型 
    }, 
    { 
      "name": "free",
      "config": { 
        "deviceType": [  //定义free支持的设备类型为2in1
          "2in1" 
        ] 
      } 
    }
  ] 
}
```

### 定义C++工程依赖的.so文件

在 C++ 工程中，可以对每个target依赖的.so文件进行定制。例如某模块依赖了function1.so、function2.so和function3.so三个文件，其中target为default的产物依赖了function1.so和function2.so；其中target为vip的产物依赖了function1.so和 function3.so，则示例代码如下所示：

```json5
{
  "apiType": 'stageMode',
  "buildOption": {
    "externalNativeOptions": {
      "path": "./src/main/cpp/CMakeLists.txt",
      "arguments": [],
      "abiFilters": [
        "arm64-v8a",
        "x86_64"
      ],
      "cppFlags": "",
    }
  },
  "targets": [  //定义不同的target 
    {
      "name": "default",
      "config": {
        "buildOption": {
          "nativeLib": {
            "filter": {
              //按照.so文件的优先级顺序，打包最高优先级的function1.so文件 
              "pickFirsts": [
                "**/function1.so"
              ],
              //排除不打包的function3.so文件 
              "excludes": [
                "**/function3.so"
              ],
              //允许当.so中资源重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件 
              "enableOverride": true
            }
          }
        }
      }
    },
    {
      "name": "vip",
      "config": {
        "buildOption": {
          "nativeLib": {
            "filter": {
              //按照.so文件的优先级顺序，打包最高优先级的function1.so文件 
              "pickFirsts": [
                "**/function1.so"
              ],
              //排除不打包的function2.so文件 
              "excludes": [
                "**/function2.so"
              ],
              //允许当.so中资源重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件 
              "enableOverride": true
            }
          }
        }
      }
    }
  ]
}
```

### 定义产物的资源

每个target使用的资源文件可能存在差异，在开发过程中，开发者可以将每个target所使用的资源存放在不同的资源目录下。其中，ArkTS工程支持对main目录下的资源文件目录（resource）进行定制；JS工程支持对main目录下的资源文件目录（resource）及 Ability下的资源文件目录（res）进行定制。如下为ArkTS工程的资源文件目录定制示例：

```json5
{ 
  "apiType": 'stageMode', 
  "buildOption": { 
  }, 
  "targets": [ 
    { 
      "name": "default",
      "resource": {  //定义默认版target使用的资源文件目录 
        "directories": [ 
          "./src/main/resources_default" 
        ] 
      } 
    }, 
    { 
      "name": "free", 
      "config": { 
        "deviceType": [ 
          "2in1" 
        ] 
      }, 
      "resource": {  //定义免费版target使用的资源文件目录 
        "directories": [ 
          "./src/main/resources_free",
          "./src/main/resources_default"
        ] 
      } 
    },
  ] 
}
```

### 定义产物的source源码集-sourceRoots

请参考[定义产物的source源码集-sourceRoots](ide-customized-multi-targets-and-products-guides.md#section18668905913)。

## 配置APP多目标构建产物

APP用于应用/元服务上架发布，针对不同的应用场景，可以定制不同的product，每个product中支持对bundleName、bundleType、签名信息、icon和label以及包含的target进行定制。

**定义目标产物product**

每一个product对应一个定制的APP包，因此，在定制APP多目标构建产物前，应提前规划好需要定制的product名称。例如，定义productA和productB。工程级build-profile.json5文件示例如下：

在定制product时，必须存在"default"的product，否则编译时会出现错误。

**说明** 

在编译构建流程中，default product或者default target都承载着兜底机制，其中，default target可以缺省。当某个模块的default target缺省时，Hvigor会默认加上default target并挂载到default product中，因此，构建default product时，默认会构建出default target。如果不想构建出default target，建议参考[定义product中包含的target](ide-customized-multi-targets-and-products-guides.md#section7613106105114)，自定义product以及包含的target。

```json5
"app": { 
  "signingConfigs": [], 
  "products": [ 
    { 
      "name": "default", 
      "signingConfig": "default", 
      "compatibleSdkVersion": "26.0.0", 
      "runtimeOS": "HarmonyOS", 
    }, 
    { 
      "name": "productA", 
      "compatibleSdkVersion": "26.0.0", 
      "runtimeOS": "HarmonyOS", 
    }, 
    { 
      "name": "productB", 
      "compatibleSdkVersion": "26.0.0", 
      "runtimeOS": "HarmonyOS", 
    } 
  ], 
  "buildModeSet": [ 
    { 
      "name": "debug", 
    }, 
    { 
      "name": "release" 
    } 
  ] 
}
```

### 定义产物的APP包名和供应商名称

每一个product均可以指定产物命名和供应商名称。

```json5
{ 
  "app": { 
    "signingConfigs": [], 
    "products": [ 
      { 
        "name": "default", 
        "signingConfig": "default", 
        "compatibleSdkVersion": "26.0.0", 
        "runtimeOS": "HarmonyOS", 
        "output": { 
          "artifactName": "customizedProductOutputName-1.0.0"  //产物名称为customizedProductOutputName-1.0.0
        }, 
        "vendor": "customizedProductVendorName"   //供应商名称为customizedProductVendorName
      }, 
      { 
        "name": "productA", 
        "compatibleSdkVersion": "26.0.0", 
        "runtimeOS": "HarmonyOS", 
        "output": { 
          "artifactName": "customizedProductOutputNameA-1.0.0"  //产物名称为customizedProductOutputNameA-1.0.0
        }, 
        "vendor": "customizedProductVendorNameA"   //供应商名称为customizedProductVendorNameA
      }, 
      { 
        "name": "productB", 
        "compatibleSdkVersion": "26.0.0", 
        "runtimeOS": "HarmonyOS", 
        "output": { 
          "artifactName": "customizedProductOutputNameB-1.0.0" //产物名称为customizedProductOutputNameB-1.0.0
        }, 
        "vendor": "customizedProductVendorNameB"   //供应商名称为customizedProductVendorNameB
      } 
    ], 
    "buildModeSet": [ 
      { 
        "name": "debug", 
      }, 
      { 
        "name": "release" 
      } 
    ] 
  }, 
}
```

如果已配置签名，product产物对应的APP包名为开发者定制的名称；如果未配置签名，product产物对应的APP包名为开发者定制的名称+unsigned。

### 定义product的bundleName

针对每个定义的product，均可以定制不同的bundleName，如果product未定义bundleName，则采用工程默认的bundleName。示例如下所示：

```json5
"app": { 
  "signingConfigs": [], 
  "products": [ 
    { 
      "name": "default", 
      "signingConfig": "default",
      "compatibleSdkVersion": "26.0.0", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example00.com"  //定义default的bundleName信息 
    }, 
    { 
      "name": "productA", 
      "signingConfig": "default", 
      "compatibleSdkVersion": "26.0.0", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example01.com"  //定义productA的bundleName信息
    }, 
    { 
      "name": "productB", 
      "signingConfig": "default",
      "compatibleSdkVersion": "26.0.0", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example02.com"  //定义productB的bundleName信息 
    } 
  ], 
  "buildModeSet": [ 
    { 
      "name": "debug", 
    }, 
    { 
      "name": "release" 
    } 
  ] 
}
```

### 定义product的bundleType

针对每个定义的product，均可以定制不同的bundleType。开发者可以通过定义每个product的bundleType，分别定义产物类型：

* bundleType值为app，表示产物为应用；
* bundleType值为atomicService，表示产物为元服务。

如果product未定义bundleType，则采用工程的bundleType（即创建工程时选择的Application/Atomic Service）。示例如下所示：

```json5
"app": { 
  "signingConfigs": [], 
  "products": [ 
    { 
      "name": "default", 
      "signingConfig": "default",
      "compatibleSdkVersion": "26.0.0", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example00.com",   
      "bundleType": "app" //定义default的bundleType信息 
    },
    { 
      "name": "productA", 
      "signingConfig": "default",
      "compatibleSdkVersion": "26.0.0", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example01.com",    
      "bundleType": "atomicService"  //定义productA的bundleType信息 
    },
    { 
      "name": "productB", 
      "signingConfig": "default",
      "compatibleSdkVersion": "26.0.0", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example02.com",    
      "bundleType": "atomicService"  //定义productB的bundleType信息 
    } 
  ], 
  "buildModeSet": [ 
    { 
      "name": "debug", 
    },
    { 
      "name": "release"
    } 
  ] 
}
```

### 定义product的签名配置信息

针对每个定义的product，均可以定制不同的signingConfig签名文件，如果product未定义signingConfig，则构建生成未签名的APP包。

通常情况下，您首先需要在签名配置界面或工程的build-profile.json5文件中配置签名信息。例如在**File > Project Structure > Project > Signing Configs**界面，分别配置default、productA和productB的签名信息，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/-ywLRYjERu6l9TRlF-qqbQ/zh-cn_image_0000002731382535.png)

签名信息配置完成后，再添加各个product对应的签名文件，示例如下所示：

您也可以提前在product中定义签名文件信息，然后在签名界面对每个product进行签名，确保配置的product签名文件与签名界面配置的签名文件保持一致即可。

```json5
"app": { 
  "signingConfigs": [], //此处通过界面配置签名后会自动生成相应的签名配置，本文略 
  "products": [ 
    { 
      "name": "default", 
      "signingConfig": "default", //定义default的签名文件信息
      "compatibleSdkVersion": "26.0.0", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example00.com"  
    }, 
    { 
      "name": "productA", 
      "signingConfig": "productA", //定义productA的签名文件信息
      "compatibleSdkVersion": "26.0.0", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example01.com"  
    }, 
    { 
      "name": "productB", 
      "signingConfig": "productB", //定义productB的签名文件信息
      "compatibleSdkVersion": "26.0.0", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example02.com" 
    } 
  ], 
  "buildModeSet": [ 
    { 
      "name": "debug", 
    }, 
    { 
      "name": "release" 
    } 
  ] 
}
```

### 定义product的icon和label

针对每个定义的product，均可以定制不同的icon和label，如果product未定义icon和label，则采用工程默认的icon和label。示例如下所示：

**说明** 

products中的icon和label字段在编译时会替换[app.json5](app-configuration-file.md)中对应的字段，app.json5和module.json5均可以配置这两个字段，如果都配置，优先级顺序请参考[配置优先级](layered-image.md#配置优先级和生成策略)。

```json5
{
  "app": {
    "signingConfigs": [],
    "products": [
      {
        "name": "default",
        "signingConfig": "default",
        "compatibleSdkVersion": "26.0.0",
        "runtimeOS": "HarmonyOS",
        "icon":"$media:default_icon", //定义default的icon
        "label":"$string:default_name", //定义default的label
      },
      {
        "name": "productA",
        "signingConfig": "default",
        "compatibleSdkVersion": "26.0.0",
        "icon":"$media:productA_icon", //定义productA的icon
        "label":"$string:productA_name", //定义productA的label
      },
      {
        "name": "productB",
        "signingConfig": "default",
        "compatibleSdkVersion": "26.0.0",
        "runtimeOS": "HarmonyOS",
        "icon":"$media:productB_icon", //定义productB的icon
        "label":"$string:productB_name",  //定义productB的label
      }
    ],
    "buildModeSet": [
      {
        "name": "debug",
      },
      {
        "name": "release"
      }
    ]
  },
  ...
}
```

### 定义product中包含的target

开发者可以选择将定义的target分别打包到哪一个product中，每个product可以指定一个或多个target。

同时每个target也可以打包到不同的product中，但是同一个module的不同target不能打包到同一个product中（除非该module的不同target配置了不同的deviceType或distributionFilter/distroFilter）。

例如，前面定义了default、free和pay三个target，现需要将default target打包到default product中；将free target打包到productA中；将pay target打包到productB中，对应的示例代码如下所示：

```json5
{ 
  "app": { 
    "signingConfigs": [], //此处通过界面配置签名后会自动生成相应的签名配置，本文略 
    "products": [ 
      { 
        "name": "default", 
        "signingConfig": "default",
        "compatibleSdkVersion": "26.0.0", 
        "runtimeOS": "HarmonyOS", 
        "bundleName": "com.example00.com"  
      }, 
      { 
        "name": "productA", 
        "signingConfig": "productA",
        "compatibleSdkVersion": "26.0.0", 
        "runtimeOS": "HarmonyOS", 
        "bundleName": "com.example01.com"  
      }, 
      { 
        "name": "productB", 
        "signingConfig": "productB",  
        "compatibleSdkVersion": "26.0.0", 
        "runtimeOS": "HarmonyOS", 
        "bundleName": "com.example02.com" 
      } 
    ], 
  "modules": [ 
    { 
      "name": "entry", 
      "srcPath": "./entry", 
      "targets": [ 
        { 
          "name": "default",  //将default target打包到default APP中 
          "applyToProducts": [ 
            "default" 
          ] 
        }, 
        { 
          "name": "free",  //将free target打包到productA APP中 
          "applyToProducts": [ 
            "productA" 
          ] 
        }, 
        { 
          "name": "pay",  //将pay target打包到productB APP中 
          "applyToProducts": [ 
            "productB" 
          ] 
        } 
      ] 
    } 
  ] 
}
```

## 构建定义的目标产物

每个target对应一个HAP，每个product对应一个APP包，在编译构建时，如果存在多product或多target时，您可以指定编译具体的包。

单击右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/MxoXNUZ1RgeXkc9JB0PlOg/zh-cn_image_0000002731382527.png)图标，指定需要打包的**Product**及**Target**，然后单击**Apply**保存。例如选择"ProductA"中，entry模块对应的"free" Target。

* **Product**：选择需要构建的APP包。
* **Build Mode**：选择[编译模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)。
* **Product Info**：该APP包的BundleName和SigningConfig信息。
* **Target Select**：选择各个模块的Target，该Target需要包含在定义的Product中才能选择，如果未包含则显示"No Target to apply"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/RO9h4WRwSMmCMO0LXc_BNQ/zh-cn_image_0000002701663304.png)

然后执行编译构建APP/HAP的任务：

* 单击菜单栏的**Build > Build Hap(s)/APP(s) > Build APP(s)** ，构建指定的Product对应的APP。例如，按照[上述配置文件](ide-customized-multi-targets-and-products-guides.md#section7613106105114)和上图中的配置，此时DevEco Studio将构建生成ProductA的APP包。default和ProductB的APP均不会生成。
* 单击菜单栏的**Build > Build Hap(s)/APP(s) > Build Hap(s)**，构建指定Product下的所有Target对应的HAP。

如果您想将某个模块下的指定target打包生成HAP，可以在工程目录中，单击模块名，然后再单击**Build > Make Module** **‘模块名** **’**，此时DevEco Studio将构建生成模块下指定target对应的包。例如，按照上述配置，此时DevEco Studio将构建生成entry模块下free的HAP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/oCA7XbohQD-C5fn5tVinsg/zh-cn_image_0000002701823224.png)

## 调试和运行指定的Target

使用DevEco Studio调试或运行应用/元服务时，每个模块只能选择其中的一个target运行，可以通过单击右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/q6zmuvZWS1qUxN7qvRqH3Q/zh-cn_image_0000002701823228.png)图标，指定需要调试或运行的**Product**下对应的**Module Target**，然后单击**Apply**保存。

**说明** 

在选择需要调试或运行的target时，需要注意选择该target所属的Product，否则将找不到可调试和运行的target。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/WeWDzarKRe6aJEesGvrqCQ/zh-cn_image_0000002701663306.png)

## 多产物构建target

* align target

  编译构建时，优先级最高的target。工程配置align target后，如果模块中存在align target，那么将自动选择align target进行构建。align target作用范围是整个工程，只能配置一个，支持命令行和配置文件两种方式。

  + 命令行方式示例如下：

    ```bash
    hvigorw -c properties.ohos.align.target=target1 assembleHap
    ```
  + 在hvigor-config.json5配置文件中添加ohos.align.target，示例如下：

    ```json5
    "properties": {
      'ohos.align.target': 'target1'
    },
    ```

* fallback target

  当模块不存在指定的target时会选用default进行构建，但如果不想用default进行构建，那么可以配置fallback target，当找不到指定target时，如果模块中存在fallback target，则使用fallback target进行构建。fallback target作用范围是整个工程，可配置多个，配置多个时按数组顺序先命中的生效。

  + 命令行方式示例如下：

    ```bash
    hvigorw -c properties.ohos.fallback.target=target1,target2 assembleHap
    ```
  + 在hvigor-config.json5配置文件中添加ohos.fallback.target，示例如下：

    ```json5
    "properties": {
      'ohos.fallback.target': ['target1', 'target2']
    }
    ```

**说明** 

* align target和fallback target配置方式命令行优先级高于配置文件。

* 使用配置文件配置align target和fallback target，仅支持DevEco Studio界面**Build**菜单栏功能，不支持**Run**菜单栏功能，可通过[hdc命令行工具](hdc.md)进行推包运行、调试。

多个target的优先级顺序为：align target > 命令行指定模块target > 父级模块target > fallback target > default。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/C9NXSh8qSMWE37hAbbIPUQ/zh-cn_image_0000002731542507.png)

举例说明：

工程依赖entry->lib1->lib2，需要构建多个产品A、B、C，工程中target配置如下：

entry: A、B、default

lib1: B、C、default

lib2: A、C、default

指定align target为A，fallback target为C。那么构建hap时的编译命令为：

```bash
hvigorw --mode module -p module=entry -c properties.ohos.align.target=A -c properties.ohos.fallback.target=C assembleHap
```

编译的target选择就是：entry@A, lib1@C, lib2@A。

**说明** 

以上所有说明仅针对非ohosTest模式。在ohosTest模式下，依赖的target固定为default，其他target均不生效。

## 使用插件配置多目标依赖

从26.0.0版本开始，支持通过@ohos/hvigor-multi-target-package-plugin插件，按照target、product和buildMode维度个性化配置依赖（dependencies和dynamicDependencies），从而构建多目标产物。

### 安装与导入插件

1. @ohos/hvigor-multi-target-package-plugin插件上架在npm中心仓，需要确保.npmrc中已配置仓库地址。

   ```txt
   @ohos:registry=https://repo.harmonyos.com/npm/
   ```
2. 在工程的hvigor-config.json5文件中配置依赖的插件。

   ```json5
   // hvigor-config.json5
   "dependencies": {
     "@ohos/hvigor-multi-target-package-plugin": "7.0.0"
   },
   ```
3. 执行Sync，DevEco Studio会自动安装依赖。
4. 在工程级hvigorfile.ts中导入插件，示例如下。

   ```ts
   // 工程级hvigorfile.ts
   import { appTasks } from '@ohos/hvigor-ohos-plugin';
   import { assembleSeqPlugin } from '@ohos/hvigor-multi-target-package-plugin';

   export default {
     system: appTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
     plugins: [assembleSeqPlugin()] // 注册插件
   }
   ```
5. 再次执行Sync即可导入插件。导入成功后，可在Hvigor任务树中看到以Seq结尾的新增任务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/XTO24s6cRXGPReIcICVRgw/zh-cn_image_0000002731382531.png)

### 配置依赖

安装并导入插件后，可以配置多目标依赖，进行代码开发及编译打包。

* 配置字段规范

  支持按target、product和buildMode三种维度配置依赖，配置字段如下，其中xxx代表target/product/buildMode的名称。

  + target：xxxTargetDependencies、xxxTargetDynamicDependencies
  + product：xxxProductDependencies、xxxProductDynamicDependencies
  + buildMode：xxxBuildModeDependencies、xxxBuildModeDynamicDependencies
* 配置位置与生效范围

  不同维度的依赖需配置在特定的oh-package.json5文件中，配置错误将不生效。

  | 依赖维度 | 配置位置 | 说明 |
  | --- | --- | --- |
  | target | 模块级oh-package.json5 | 仅支持在模块级配置。 |
  | product | 工程级oh-package.json5 | 仅支持在工程级配置。 |
  | buildMode | 工程级或模块级oh-package.json5 | 说明：  建议二选一，统一在工程级或模块级中配置，避免混合配置。  插件不会对同时配置在工程级和模块级oh-package.json5中的buildMode级别依赖进行合并处理。 |

* 依赖优先级

  target级 > product级 > buildMode级

* 配置示例

  ```json5
  // 工程级oh-package.json5
  "phoneProductDependencies": {
      "dialog": "1.0.1"
  },
  "debugBuildModeDependencies": {    // 工程级和模块级二选一配置
    "dialog": "1.0.0"
  }
  "phoneProductDynamicDependencies": {
    "dialog": "1.0.1"
  },
  "debugBuildModeDynamicDependencies": {    // 工程级和模块级二选一配置
    "dialog": "1.0.0"
  },

  // 模块级oh-package.json5
  "debugBuildModeDependencies": {    // 工程级和模块级二选一配置
    "dialog": "1.0.0"
  },
  "phoneTargetDependencies": {
    "dialog": "1.0.2"
  },
  "debugBuildModeDynamicDependencies": {    // 工程级和模块级二选一配置
    "dialog": "1.0.0"
  },
  "phoneTargetDynamicDependencies": {
    "dialog": "1.0.2"
  }
  ```

### 定制产物版本号

对于HAR或者HSP，当不同target使用不同的依赖时，为避免不同target的产物使用相同版本号导致难以区分，可通过配置文件assemble-seq-plugin-config.json5为不同target的版本号添加后缀。

如下示例，两个target产物生成的版本号分别为：${version}.default和${version}.phone，其中${version}是模块级oh-package.json5中的version字段值。

```json5
// assemble-seq-plugin-config.json5，放在每个模块的根目录下
{
  "targets": [
    {
      "name": "default",
      "output": {
          "versionSuffix": ".default"
      }
    },
    {
      "name": "phone",
      "output": {
        "versionSuffix": ".phone"
      }
    }
  ]
}
```

### 编译打包

配置完成后，在DevEco Studio的Hvigor任务树中，找到并双击执行以Seq结尾的任务，即可完成编译打包。
