---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-example-of-the-operator-json
title: 算子json配置文件样例
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 附录 > 调测工具样例与参数说明 > 算子json配置文件样例
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:05+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:f0160ee5d2709f92f1beb1cc78a6f2fcd255afd9a7619634eabcadecce873f29
---

## 样例1：NPU/CPU调测算子json配置文件样例

**说明** 

* 在"param\_type"："optional"时，"ignore"为true，表示不需要该输入；"ignore"为false，表示需要该输入。
* 在"param\_type"："required"时，"ignore"不能配置为true。

```json
{
  "op_type": "FlashAttentionScore",
  "data_script": "./flash_attention_score_golden.py",
  "gen_data": true,
  "inputs": [
    {
      "name": "query",
      "dtype": "float16",
      "format": "ND",
      "ignore": false,
      "shape": [24,144,1280],
      "param_type": "required",
      "data_file": "q.bin"
    },
    {
      "name": "key",
      "dtype": "float16",
      "format": "ND",
      "ignore": false,
      "shape": [24,144,1280],
      "param_type": "required",
      "data_file": "k.bin"
    },
    {
      "name": "value",
      "dtype": "float16",
      "format": "ND",
      "ignore": false,
      "shape": [24,144,1280],
      "param_type": "required",
      "data_file": "v.bin"
    },
  ],
  "outputs": [
    {
      "name": "softmax_max",
      "dtype": "float32",
      "format": "ND",
      "shape": [24,20,144,8],
      "ignore": false,
      "param_type": "required",
      "data_file": null
    },
    {
      "name": "softmax_sum",
      "dtype": "float32",
      "format": "ND",
      "shape": [24,20,144,8],
      "ignore": false,
      "param_type": "required",
      "data_file": null
    },
    {
      "name": "softmax_out",
      "dtype": "float16",
      "format": "ND",
      "shape": [24,20,144,144],
      "ignore": false,
      "param_type": "required",
      "data_file": null
    },
    {
      "name": "attention_out",
      "dtype": "float16",
      "format": "ND",
      "shape": [24,20,144,64],
      "ignore": false,
      "param_type": "required",
      "data_file": "attention_out.bin"
    }
  ],
  "attrs": [
    {
      "name": "scale_value",
      "dtype": "float",
      "value": 1.0
    },
    {
      "name": "keep_prob",
      "dtype": "float",
      "value": 0.8
    },
    {
      "name": "pre_tokens",
      "dtype": "int",
      "value": 2147483647
    },
    {
      "name": "next_tokens",
      "dtype": "int",
      "value": 2147483647
    },
    {
      "name": "head_num",
      "dtype": "int",
      "value": 20
    },
    {
      "name": "input_layout",
      "dtype": "string",
      "value": "BSH"
    },
    {
      "name": "inner_precise",
      "dtype": "int",
      "value": 0
    }
  ]
}
```

## 样例2：tensor list json配置文件样例

```json
{
  "op_type": "IncreFlashAttention",
  "data_script": "",
  "gen_data": false,
  "inputs": [
      {
          "name": "query",
          "dtype": "float16",
          "format": "ND",
          "ignore": false,
          "shape": [4, 5, 1, 128],
          "param_type": "required",
          "data_file": "/home/data/input/q.bin"
      },
      [{
          "name": "key0",
          "dtype": "float16",
          "format": "ND",
          "ignore": false,
          "shape": [1,5,8192,128],
          "param_type": "required",
          "data_file": "/home/data/input/k_0.bin"
      },{
          "name": "key1",
          "dtype": "float16",
          "format": "ND",
          "ignore": false,
          "shape": [1,5,8192,128],
          "param_type": "required",
          "data_file": "/home/data/input/k_1.bin"
      },{
          "name": "key2",
          "dtype": "float16",
          "format": "ND",
          "ignore": false,
          "shape": [1,5,8192,128],
          "param_type": "required",
          "data_file": "/home/data/input/k_2.bin"
      },{
          "name": "key3",
          "dtype": "float16",
          "format": "ND",
          "ignore": false,
          "shape": [1,5,8192,128],
          "param_type": "required",
          "data_file": "/home/data/input/k_3.bin"
      }],
      [{
          "name": "value0",
          "dtype": "float16",
          "format": "ND",
          "ignore": false,
          "shape": [1,5,8192,128],
          "param_type": "required",
          "data_file": "/home/data/input/v_0.bin"
      },{
          "name": "value1",
          "dtype": "float16",
          "format": "ND",
          "ignore": false,
          "shape": [1,5,8192,128],
          "param_type": "required",
          "data_file": "/home/data/input/v_1.bin"
      },{
          "name": "value2",
          "dtype": "float16",
          "format": "ND",
          "ignore": false,
          "shape": [1,5,8192,128],
          "param_type": "required",
          "data_file": "/home/data/input/v_2.bin"
      },{
          "name": "value3",
          "dtype": "float16",
          "format": "ND",
          "ignore": false,
          "shape": [1,5,8192,128],
          "param_type": "required",
          "data_file": "/home/data/input/v_3.bin"
      }],
      {
          "name": "padding_mask",
          "dtype": "float16",
          "format": "ND",
          "ignore": false,
          "shape": null,
          "param_type": "optional",
          "data_file": null
      },
      {
          "name": "atten_mask",
          "dtype": "float16",
          "format": "ND",
          "ignore": false,
          "shape": [4,1,8192],
          "param_type": "optional",
          "data_file": "/home/data/input/attenMask.bin"
      },
      {
          "name": "actual_seq_lengths",
          "dtype": "int64",
          "format": "ND",
          "ignore": false,
          "shape": null,
          "param_type": "optional",
          "data_file": ""
      },
      {
          "name": "deq_scale1",
          "dtype": "uint64",
          "format": "ND",
          "ignore": false,
          "shape": null,
          "param_type": "optional",
          "data_file": null
      },
      {
          "name": "quant_scale1",
          "dtype": "float32",
          "format": "ND",
          "ignore": false,
          "shape": null,
          "param_type": "optional",
          "data_file": null
      },
      {
          "name": "deq_scale2",
          "dtype": "uint64",
          "format": "ND",
          "ignore": false,
          "shape": null,
          "param_type": "optional",
          "data_file": null
      },
      {
          "name": "quant_scale2",
          "dtype": "float32",
          "format": "ND",
          "ignore": false,
          "shape": null,
          "param_type": "optional",
          "data_file": null
      },
      {
          "name": "quant_offset2",
          "dtype": "float32",
          "format": "ND",
          "ignore": false,
          "shape": null,
          "param_type": "optional",
          "data_file": null
      }
  ],
  "outputs": [
      {
          "name": "attention_out",
          "dtype": "float16",
          "format": "ND",
          "shape": [4, 5, 1, 128],
          "ignore": false,
          "param_type": "required",
          "data_file": "/home/data/output/y_add.bin"
      }
  ],
  "attrs": [
      {
          "name": "num_heads",
          "dtype": "int",
          "value": 5
      },
      {
          "name": "scale_value",
          "dtype": "float",
          "value": 2.0
      },
      {
          "name": "input_layout",
          "dtype": "string",
          "value": "BNSD"
      },
      {
          "name": "num_key_value_heads",
          "dtype": "int",
          "value": 5
      }
  ]}
```

## 样例3：tiling调测json配置文件样例

```json
{
  "op_type": "FlashAttentionScore",
  "data_script": "./flash_attention_score_golden.py",
  "gen_data": true,
  "inputs": [
    {
      "name": "query",
      "dtype": "float16",
      "format": "ND",
      "ignore": false,
      "shape": [24,144,1280],
      "param_type": "required",
      "data_file": "q.bin"
    },
    {
      "name": "key",
      "dtype": "float16",
      "format": "ND",
      "ignore": false,
      "shape": [24,144,1280],
      "param_type": "required",
      "data_file": "k.bin"
    },
    {
      "name": "value",
      "dtype": "float16",
      "format": "ND",
      "ignore": false,
      "shape": [24,144,1280],
      "param_type": "required",
      "data_file": "v.bin"
    },
    {
      "name": "real_shift",
      "dtype": "float16",
      "format": "ND",
      "ignore": false,
      "shape": null,
      "param_type": "optional",
      "data_file": null
    },
    {
      "name": "drop_mask",
      "dtype": "uint8",
      "format": "ND",
      "ignore": false,
      "shape": [1244160],
      "param_type": "optional",
      "data_file": "drop_mask.bin"
    },
    {
      "name": "padding_mask",
      "dtype": "float16",
      "format": "ND",
      "ignore": false,
      "shape": null,
      "param_type": "optional",
      "data_file": null
    },
    {
      "name": "atten_mask",
      "dtype": "bool",
      "format": "ND",
      "ignore": false,
      "shape": null,
      "param_type": "optional",
      "data_file": null
    },
    {
      "name": "prefix",
      "dtype": "int64",
      "format": "ND",
      "ignore": false,
      "shape": null,
      "param_type": "optional",
      "data_file": null
    }
  ],
  "outputs": [
    {
      "name": "softmax_max",
      "dtype": "float32",
      "format": "ND",
      "shape": [24,20,144,8],
      "ignore": false,
      "param_type": "required",
      "data_file": null
    },
    {
      "name": "softmax_sum",
      "dtype": "float32",
      "format": "ND",
      "shape": [24,20,144,8],
      "ignore": false,
      "param_type": "required",
      "data_file": null
    },
    {
      "name": "softmax_out",
      "dtype": "float16",
      "format": "ND",
      "shape": [24,20,144,144],
      "ignore": false,
      "param_type": "required",
      "data_file": null
    },
    {
      "name": "attention_out",
      "dtype": "float16",
      "format": "ND",
      "shape": [24,20,144,64],
      "ignore": false,
      "param_type": "required",
      "data_file": "attention_out.bin"
    }
  ],
  "attrs": [
    {
      "name": "scale_value",
      "dtype": "float",
      "value": 1.0
    },
    {
      "name": "keep_prob",
      "dtype": "float",
      "value": 0.8
    },
    {
      "name": "pre_tokens",
      "dtype": "int",
      "value": 2147483647
    },
    {
      "name": "next_tokens",
      "dtype": "int",
      "value": 2147483647
    },
    {
      "name": "head_num",
      "dtype": "int",
      "value": 20
    },
    {
      "name": "input_layout",
      "dtype": "string",
      "value": "BSH"
    },
    {
      "name": "inner_precise",
      "dtype": "int",
      "value": 0
    }
  ]
}
```

## 样例4：kernel直调json配置样例

```json
{
    "op_type": "add_custom",
    "data_script": "",
    "gen_data": false,
    "params": [
            {
                "name": "x",
                "dtype": "float16",
                "param_type": "input",
                "shape": [
                    1,16384
                ],
                "data_file": "input_x.bin"
            },
            {
                "name": "y",
                "dtype": "float16",
                "param_type": "input",
                "shape": [
                    1,16384
                ],
                "data_file": "input_y.bin"
            },
            {
                "name": "z",
                "dtype": "float16",
                "param_type": "output",
                "shape": [
                    1,16384
                ],
                "data_file": "golden.bin"
            },
            {
                "name": "tileNumIn",
                "dtype": "uint32",
                "param_type": "input",
                "shape": null,
                "data_value": 8
            }
    ],
    "kernel_info": {
        "kernel_source": ["add_custom.cpp"],
        "kernel_name": "add_custom",
        "kernel_includes": []
    }
 
}
```
