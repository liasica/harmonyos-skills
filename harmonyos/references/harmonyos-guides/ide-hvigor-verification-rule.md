---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-verification-rule
title: HAP唯一性校验逻辑
breadcrumb: 指南 > 构建应用 > 配置构建流程 > HAP唯一性校验逻辑
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:56+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:1a6030a7f1ade3543bce482592698e52916d1586217d7bc8f3aaaecfdefa5f70
---

HAP是应用安装的基本单位，在DevEco Studio工程目录中，一个HAP对应一个Module。应用打包时，每个Module生成一个.hap文件。

应用如果包含多个Module，在应用市场上架时，会将多个.hap文件打包成一个.app文件（称为Bundle），但在云端分发和端侧安装时，仍然是以HAP为基本单位。

为了能够正常分发和安装应用，需要保证一个应用安装到设备时，Module的名称、Ability的名称不重复，并且只有一个Entry类型的Module与目标设备相对应。

DevEco Studio会在编译构建时，对HAP进行上述唯一性校验，如果校验不通过，将会编译失败或给出告警。

## Module校验逻辑

校验目的：同一目标设备上Module唯一。

1. 校验Module的Name。如果多个Module的Name不同，则校验通过。如果Name相同，继续校验deviceType。
2. 校验设备类型deviceType。如果deviceType不相交，则校验通过。如果deviceType相交，继续校验distributionFilter。

   deviceType不相交是指两个Module的deviceType中配置了完全不同的设备，例如：

   ```json5
   //Module1和Module2配置了完全不同的设备，deviceType不相交。
   //Module1
   {
     "deviceType": ["tv", "tablet"]
   }
   //Module2
   {
     "deviceType": ["car"]
   }
   ```

   deviceType相交是指两个Module的deviceType中包含了相同的设备，例如：

   ```json5
   //Module1和Module2因为都包含"tablet"设备，导致deviceType相交。
   //Module1
   {
     "deviceType": ["tv", "tablet"]
   }
   //Module2
   {
     "deviceType": ["car", "tablet"]
   }
   ```
3. 校验分发规则distributionFilter。如果distributionFilter不相交，则校验通过。如果distributionFilter相交，则无法保证Module唯一性，校验失败，打包失败。

   distributionFilter中包含属性apiVersion、screenShape、screenWindow、screenDensity和countryCode，相交的相关含义如下：

   * distributionFilter不相交：如果两个distributionFilter中任意一个属性不相交，则两个distributionFilter不相交。
   * distributionFilter相交：如果两个distributionFilter中所有属性都相交，则两个distributionFilter相交。

   例如，两 Module 中的apiVersion、screenShape、screenWindow、screenDensity都相交，但countryCode不相交，则可以区分两个Module，校验通过。

   ```json5
   //Module1和Module2的两个distributionFilter中，countryCode不相交，则两个distributionFilter不相交。
   //Module1
   {
     "distributionFilter": {
       "apiVersion" : {
         "policy": "include",
         "value": [10,11]
       },
       "screenShape": {
         "policy": "include",
         "value": ["rect"]
       },
       "screenWindow": {
         "policy": "include",
         "value": ["454*454", "466*466"]
       },
       "screenDensity": {
         "policy": "include",
         "value": ["ldpi", "xldpi"]
       },
       "countryCode": {
         "policy": "include",
         "value": ["CN", "HK"]
       }
     }
   }
   //Module2
   {
     "distributionFilter": {
       "apiVersion" : {
         "policy": "include",
         "value": [10,11]
       },
       "screenShape": {
         "policy": "include",
         "value": ["rect"]
       },
       "screenWindow": {
         "policy": "include",
         "value": ["454*454", "466*466"]
       },
       "screenDensity": {
         "policy": "include",
         "value": ["ldpi", "xldpi"]
       },
       "countryCode": {
         "policy": "include",
         "value": ["USA", "UK"]
       }
     }
   }
   ```

## Ability校验逻辑

校验目的：同一目标设备上Ability唯一。

1. 校验Ability的Name。如果多个Ability的Name不同，则校验通过。如果Name相同，继续校验Ability所属Module的deviceType。
2. 校验Ability所属Module的deviceType。如果deviceType不相交，校验通过。如果deviceType相交，继续校验Ability所属Module的distributionFilter。

   例如，两个Ability的Name相同，但其所属Module的deviceType不相交，校验通过。

   ```json5
   //Ability1和Ability2虽然名称相同，但由于其所属Module的deviceType不相交，所以可以区分两个Ability，校验通过。
   //Ability1
   {
     "module": {
       "name": "module_sample1",
       "deviceType": ["tv", "tablet"],
       "abilities": [
         {
           "name": "ability_sample"
         }
       ]
     }
   }
   //Ability2
   {
     "module": {
       "name": "module_sample2",
       "deviceType": ["car"],
       "abilities": [
         {
           "name": "ability_sample"
         }
       ]
     }
   }
   ```
3. 校验Ability所属Module的distributionFilter。如果distributionFilter不相交，校验通过。如果distributionFilter相交，校验失败，抛出告警。

   例如，两个Ability的Name相同，其所属Module的deviceType也相交，但其所属Module的distributionFilter不相交，校验通过。

   ```json5
   //Ability1和Ability2的Name相同，而且其所属Module的deviceType相交，但其所属Module的distributionFilter不相交，所以可以区分两个Ability，校验通过。
   //Ability1
   {
     "module": {
       "name": "module_sample",
       "deviceType": ["tv", "tablet"],
       "metadata": [
         {
           "name": "distributionFilter_config",
           "resource": "$profile:distributionFilter_config_sample1"
         }
       ],
       "abilities": [
         {
           "name": "ability_sample"
         }
       ]
     }
   }
   //Ability1所属Module的distributionFilter
   {
     "distributionFilter": {
       "apiVersion" : {
         "policy": "include",
         "value": [10,11]
       },
       "screenShape": {
         "policy": "include",
         "value": ["rect"]
       },
       "screenWindow": {
         "policy": "include",
         "value": ["454*454", "466*466"]
       },
       "screenDensity": {
         "policy": "include",
         "value": ["ldpi", "xldpi"]
       },
       "countryCode": {
         "policy": "include",
         "value": ["CN", "HK"]
       }
     }
   }

   //Ability2
   {
     "module": {
       "name": "module_sample2",
       "deviceType":  ["tv", "tablet"],
       "metadata": [
         {
           "name": "distributionFilter_config",
           "resource": "$profile:distributionFilter_config_sample2"
         }
       ],
       "abilities": [
         {
           "name": "ability_sample"
         }
       ]
     }
   }
   //Ability2所属Module的distributionFilter
   {
     "distributionFilter": {
       "apiVersion" : {
         "policy": "include",
         "value": [10,11]
       },
       "screenShape": {
         "policy": "include",
         "value": ["rect"]
       },
       "screenWindow": {
         "policy": "include",
         "value": ["454*454", "466*466"]
       },
       "screenDensity": {
         "policy": "include",
         "value": ["ldpi", "xldpi"]
       },
       "countryCode": {
         "policy": "include",
         "value": ["USA", "UK"]
       }
     }
   }
   ```

## Entry校验逻辑

校验目的：目标设备只有一个Entry类型的Module与之对应，Feature类型的Module经过deviceType及distributionFilter指明的目标设备都需要存在Entry类型的Module。

1. 校验Feature类型的Module经过deviceType及distributionFilter指明的目标设备都存在Entry类型的Module。

   例如，Bundle中存在一个Entry类型Module1，其支持设备为tablet和wearable，其分发规则为circle和rect形状的屏幕，同时存在一个Feature类型的Module2，通过分发规则可知，其可以分发到rect形状的tablet和wearable设备上，而rect形状的tablet和wearable设备上存在Entry类型的Module1，校验通过。

   ```json5
   //Entry类型Module1
   {
     "module": {
       "name": "module_sample1",
       "type": "entry",
       "deviceType": ["tablet", "wearable"],
       "metadata": [
         {
           "name": "distributionFilter_config",
           "resource": "$profile:distributionFilter_config1"
         }
       ]
     }
   }
   //Module1的distributionFilter，distributionFilter_config1.json
   {
     "screenShape":{
       "policy": "include",
       "value": ["circle", "rect"]
     }
   }
   //Feature类型Module2
   {
     "module": {
       "name": "module_sample2",
       "type": "feature",
       "deviceType": ["tablet", "wearable"],
       "metadata": [
         {
           "name": "distributionFilter_config",
           "resource": "$profile:distributionFilter_config2"
         }
       ]
     }
   }
   //Module2的distributionFilter，distributionFilter_config2.json
   {
     "screenShape":{
       "policy": "include",
       "value": ["rect"]
     }
   }
   ```
2. 校验目标设备只有一个Entry类型的Module与之对应。
   1. 校验Entry类型Module的deviceType。如果deviceType不相交，校验通过。如果deviceType相交，继续校验Entry类型Module的distributionFilter。

      例如，同一个Bundle中存在两个Entry类型的Module，分别为Module1和Module2，两者的deviceType不相交，可以有效区分两个Module，校验通过。

      ```json5
      //Entry类型Module1
      {
        "module": {
          "name": "module_sample1",
          "type": "entry",
          "deviceType": ["tablet"]
        }
      }
      //Entry类型Module2
      {
        "module": {
          "name": "module_sample2",
          "type": "entry",
          "deviceType": ["wearable"]
        }
      }
      ```
   2. 校验Entry类型Module的distributionFilter。如果distributionFilter不相交，校验通过。如果distributionFilter相交，校验失败，打包失败。

      例如，同一个Bundle中存在两个Entry类型的Module，分别为Module1和Module2，两者的deviceType相交，但两者的distributionFilter不相交，可以有效区分两个Module，校验通过。

      ```json5
      //Entry类型Module1
      {
        "module": {
          "name": "module_sample1",
          "type": "entry",
          "deviceType": ["wearable"],
          "metadata": [
            {
              "name":"distributionFilter_config",
              "resource": "$profile:distributionFilter_sample1"
            }
          ]
        }
      }
      //Module1的distributionFilter，distributionFilter_sample1.json
      {
        "distributionFilter": {
          "screenShape":{
            "policy": "include",
            "value": ["rect"]
          }
        }
      }
      //Entry类型Module2
      {
        "module": {
          "name": "module_sample2",
          "type": "entry",
          "deviceType": ["wearable"],
          "metadata": [
            {
              "name":"distributionFilter_config",
              "resource": "$profile:distributionFilter_sample2"
            }
          ]
        }
      }
      //Module2的distributionFilter，distributionFilter_sample2.json
      {
        "distributionFilter": {
          "screenShape":{
            "policy": "include",
            "value": ["circle"]
          }
        }
      }
      ```
