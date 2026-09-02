---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-data-generation-script-adaptation
title: 数据生成脚本适配样例
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 附录 > 调测工具样例与参数说明 > 数据生成脚本适配样例
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:35+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:cec34dcff2909a2055076203037ea68657908985f8586571e35e3a228f1c4e55
---

```python
import sys
import os
import json
import logging
from functools import reduce
from dataclasses import dataclass
import numpy as np
from numpy import array
DTYPE = {
    "float16": np.float16
}
atol, rtol = 0.005, 0.005
def byte_2_bit(drop_mask, size):
    print(len(drop_mask))
    drop_mask_bit = np.zeros((int(size / 8),), dtype=np.uint8)
    for i in range(int(size / 8)):
        tmp = 0
        for j in range(8):
            tmp += drop_mask[i * 8 + j] * (2 ** j)
        drop_mask_bit[i] = tmp
    return drop_mask_bit
def get_input_attrs_content(input_json: str) -> dict:
    content = {}
    input_json = os.path.realpath(input_json)
    with open(input_json, "r") as in_hadle:
        try:
            content = json.load(in_hadle)
        except json.decoder.JSONDecodeError:
            logging.error("json.decoder.JSONDecodeError")
        finally:
            pass
    return content
def softmax(x, axis=None):
    x = x.astype(np.float32)
    x_max = x.max(axis=-1, keepdims=True)
    x_sub = x - x_max
    y = np.exp(x_sub)
    x_sum = y.sum(axis=-1, keepdims=True)
    ans = y / x_sum
    ans = ans.astype(np.float16)
    x_max = x_max.astype(np.float16)
    x_sum = x_sum.astype(np.float16)
    return ans, x_max, x_sum
def attention_score(shape_info_tuple,
                    input_path,
                    output_path,
                    need_new):
    qkv_shape, drop_mask_shape, keep_prob, input_dtype, output_dtype = shape_info_tuple
    if need_new:
        q = np.random.uniform(-0.1, 0.1, qkv_shape).astype(input_dtype)
        q_trans = q.transpose(0, 2, 1, 3)
        q_trans.tofile(input_path["query"])
        k = np.random.uniform(-0.1, 0.1, qkv_shape).astype(input_dtype)
        k_trans = k.transpose(0, 2, 1, 3)
        k_trans.tofile(input_path["key"])
        v = np.random.uniform(-0.1, 0.1, qkv_shape).astype(input_dtype)
        v_trans = v.transpose(0, 2, 1, 3)
        v_trans.tofile(input_path["value"])
        if drop_mask_shape is not None:
            drop_mask = np.random.uniform(0, 2, drop_mask_shape).astype(np.uint8)
            size = reduce(lambda x, y: x * y, drop_mask_shape)
            drop_mask_bit = byte_2_bit(
                drop_mask, int(size)).reshape(qkv_shape[0], qkv_shape[1], qkv_shape[2], int(qkv_shape[2] / 8))
            drop_mask_bit.tofile(input_path["drop_mask"])
    else:
        q = np.fromfile(input_path["query"], input_dtype).reshape(qkv_shape).astype(input_dtype)
        k = np.fromfile(input_path["key"], input_dtype).reshape(qkv_shape).astype(input_dtype)
        v = np.fromfile(input_path["value"], input_dtype).reshape(qkv_shape).astype(input_dtype)
        drop_mask = np.fromfile(
            input_path["drop_mask"],
            dtype=np.uint8).reshape(qkv_shape[0], qkv_shape[1], qkv_shape[2], int(qkv_shape[2] / 8))
    qk = np.matmul(q, k.transpose(0, 1, 3, 2))
    softmax_res, x_max, x_sum = softmax(qk)
    drop_res = 1 / keep_prob * np.multiply(
        softmax_res, drop_mask.reshape(qkv_shape[0], qkv_shape[1], qkv_shape[2], qkv_shape[2]))
    y = np.matmul(drop_res, v)
    y = y.transpose(0, 2, 1, 3)
    y.astype(output_dtype).tofile(output_path["attention_out"])
    return
def gen_total_golden_output(shape_info, input_path, golden_path, need_new):
    b_value, head_num, s_value, h_value = shape_info.shape_info
    qkv_shape = [b_value, head_num, s_value, h_value // head_num]
    drop_shape = [b_value * head_num * s_value * s_value]
    attention_score((qkv_shape,
                     drop_shape,
                     shape_info.keep_prob,
                     shape_info.input_dtype,
                     shape_info.output_dtype),
                    input_path,
                    golden_path,
                    need_new)
def get_data_file(res_path, contents):
    data_files = {}
    for content in contents:
        if content["data_file"] is None:
            continue
        data_files[content["name"]] = os.path.join(res_path, content["data_file"])
    return data_files
@dataclass
class InputOutputShapeInfo:
    shape_info: tuple
    keep_prob: int
    input_dtype: np.dtype
    output_dtype: np.dtype
def get_args():
    """
    需要开发者按需配置
    sys.argv[1]: input json file path
    sys.argv[2]: output file path
    sys.argv[3]: gen data type: input/output/all
    """
    logging.info(f"数据保存路径为：{sys.argv[2]}")
    input_file = sys.argv[1]
    res_path = sys.argv[2]
    content = get_input_attrs_content(input_file)
    input_files = get_data_file(res_path, content.get("inputs"))
    output_files = get_data_file(res_path, content.get("outputs"))
    attrs = content.get("attrs")
    cmp_idx = 0
    for attr in attrs:
        if attr["name"] == "input_layout":
            input_layout = attr["value"]
            logging.info(f"get input_layout:{input_layout}")
        if attr["name"] == "keep_prob":
            keep_prob = attr["value"]
            logging.info(f"get keep_prob:{keep_prob}")
        if attr["name"] == "head_num":
            head_num = attr["value"]
            logging.info(f"get head_num:{head_num}")
    shape = content.get("inputs")[cmp_idx].get("shape")
    b_value = shape[input_layout.find("B")]
    s_value = shape[input_layout.find("S")]
    h_value = shape[input_layout.find("H")]
    input_dtype = DTYPE.get(content.get("inputs")[cmp_idx].get("dtype"), np.float16)
    output_dtype = DTYPE.get(content.get("outputs")[cmp_idx].get("dtype"), np.float16)
    shape_info = InputOutputShapeInfo(shape_info=(b_value, head_num, s_value, h_value),
                                      keep_prob=keep_prob,
                                      input_dtype=input_dtype,
                                      output_dtype=output_dtype)
    return shape_info, input_files, output_files
if __name__ == '__main__':
    """
    sys.argv[1]: input data file path
    sys.argv[2]: output file path
    sys.argv[3]: gen data type: input/output/all
    """
    tensor_shape_info, input_file_list, output_file_list = get_args()
    gen_total_golden_output(tensor_shape_info, input_file_list, output_file_list, need_new=True)
```
