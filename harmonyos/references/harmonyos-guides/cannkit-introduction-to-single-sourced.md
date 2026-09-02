---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-introduction-to-single-sourced
title: 同源算子调测样例
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 附录 > 调测工具样例与参数说明 > 同源算子调测样例
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:76a8173f028a3d085829440fc2bbb6d1da35038004380a8862fb51ae34c4d2ca
---

同源算子指算子的输入和输出为同一地址，算子在计算完成后，把原有的输出结果直接覆盖在输入的地址上，同源算子调测时，需要在outputs中配置对应的算子输出，输出名称类型要和input保持一致。

## 同源算子配置示例

tensor类：定义的json数据的object中name shape dtype format在inputs和outputs里必须一致，但是data\_file必须可区分，在调测过程中，这两个文件会同步到data的目录下，如果文件名相同，则会导致JSON文件被覆盖。

```json
{
    "op_type": "AbsCustom",
    "data_script": "./add_golden.py",
    "checkpoint_dump_path": "./debug_workspace/AddCustom/data/dump",
    "gen_data": true,
    "inputs": [
        {
            "name": "x",
            "dtype": "float16",
            "format": "ND",
            "ignore": false,
            "shape": [32],
            "param_type": "required",
            "data_file": "x.bin"
        }
         
    ],
    "outputs": [
        {
            "name": "x",
            "dtype": "float16",
            "format": "ND",
            "ignore": false,
            "shape": [32],
            "param_type": "required",
            "data_file": "ref_x.bin"
        }
    ]
     
}
```

tensorlist类：list中的每个对象必须是同源且数量位置一致。

```json
{
    "op_type": "ForeachACosInplace",
    "data_script":"ForeachACosInplace.py",
    "gen_data": true,
    "inputs": [
            [{
                "name": "inputs",
                "dtype": "float32",
                "format": "ND",
                "param_type": "required",
                "shape": [
                    10
                ],
                "data_file": "x0.bin"
            },{
                "name": "inputs1",
                "dtype": "float32",
                "format": "ND",
                "param_type": "required",
                "shape": [
                    8,8
                ],
                "data_file": "x1.bin"
            }]
    ],
    "outputs": [
        [{
            "name": "inputs",
            "dtype": "float32",
            "format": "ND",
            "param_type": "required",
            "shape": [
                10
            ],
            "data_file": "ref_x0.bin"
        },{
            "name": "inputs1",
            "dtype": "float32",
            "format": "ND",
            "param_type": "required",
            "shape": [
                8,8
            ],
            "data_file": "ref_x1.bin"
        }
      ]
    ]
}
```
