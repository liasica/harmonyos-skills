---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-data-generation-script-adaptation
title: 数据生成脚本适配样例
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 附录 > 调测工具样例与参数说明 > 数据生成脚本适配样例
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e1e7a49706ba822f37fa85092246ca2ede6c4818022ef261512b0e98a80bc4c0
---

```
1. import sys
2. import os
3. import json
4. import logging
5. from functools import reduce
6. from dataclasses import dataclass
7. import numpy as np
8. from numpy import array
9. DTYPE = {
10. "float16": np.float16
11. }
12. atol, rtol = 0.005, 0.005
13. def byte_2_bit(drop_mask, size):
14. print(len(drop_mask))
15. drop_mask_bit = np.zeros((int(size / 8),), dtype=np.uint8)
16. for i in range(int(size / 8)):
17. tmp = 0
18. for j in range(8):
19. tmp += drop_mask[i * 8 + j] * (2 ** j)
20. drop_mask_bit[i] = tmp
21. return drop_mask_bit
22. def get_input_attrs_content(input_json: str) -> dict:
23. content = {}
24. input_json = os.path.realpath(input_json)
25. with open(input_json, "r") as in_hadle:
26. try:
27. content = json.load(in_hadle)
28. except json.decoder.JSONDecodeError:
29. logging.error("json.decoder.JSONDecodeError")
30. finally:
31. pass
32. return content
33. def softmax(x, axis=None):
34. x = x.astype(np.float32)
35. x_max = x.max(axis=-1, keepdims=True)
36. x_sub = x - x_max
37. y = np.exp(x_sub)
38. x_sum = y.sum(axis=-1, keepdims=True)
39. ans = y / x_sum
40. ans = ans.astype(np.float16)
41. x_max = x_max.astype(np.float16)
42. x_sum = x_sum.astype(np.float16)
43. return ans, x_max, x_sum
44. def attention_score(shape_info_tuple,
45. input_path,
46. output_path,
47. need_new):
48. qkv_shape, drop_mask_shape, keep_prob, input_dtype, output_dtype = shape_info_tuple
49. if need_new:
50. q = np.random.uniform(-0.1, 0.1, qkv_shape).astype(input_dtype)
51. q_trans = q.transpose(0, 2, 1, 3)
52. q_trans.tofile(input_path["query"])
53. k = np.random.uniform(-0.1, 0.1, qkv_shape).astype(input_dtype)
54. k_trans = k.transpose(0, 2, 1, 3)
55. k_trans.tofile(input_path["key"])
56. v = np.random.uniform(-0.1, 0.1, qkv_shape).astype(input_dtype)
57. v_trans = v.transpose(0, 2, 1, 3)
58. v_trans.tofile(input_path["value"])
59. if drop_mask_shape is not None:
60. drop_mask = np.random.uniform(0, 2, drop_mask_shape).astype(np.uint8)
61. size = reduce(lambda x, y: x * y, drop_mask_shape)
62. drop_mask_bit = byte_2_bit(
63. drop_mask, int(size)).reshape(qkv_shape[0], qkv_shape[1], qkv_shape[2], int(qkv_shape[2] / 8))
64. drop_mask_bit.tofile(input_path["drop_mask"])
65. else:
66. q = np.fromfile(input_path["query"], input_dtype).reshape(qkv_shape).astype(input_dtype)
67. k = np.fromfile(input_path["key"], input_dtype).reshape(qkv_shape).astype(input_dtype)
68. v = np.fromfile(input_path["value"], input_dtype).reshape(qkv_shape).astype(input_dtype)
69. drop_mask = np.fromfile(
70. input_path["drop_mask"],
71. dtype=np.uint8).reshape(qkv_shape[0], qkv_shape[1], qkv_shape[2], int(qkv_shape[2] / 8))
72. qk = np.matmul(q, k.transpose(0, 1, 3, 2))
73. softmax_res, x_max, x_sum = softmax(qk)
74. drop_res = 1 / keep_prob * np.multiply(
75. softmax_res, drop_mask.reshape(qkv_shape[0], qkv_shape[1], qkv_shape[2], qkv_shape[2]))
76. y = np.matmul(drop_res, v)
77. y = y.transpose(0, 2, 1, 3)
78. y.astype(output_dtype).tofile(output_path["attention_out"])
79. return
80. def gen_total_golden_output(shape_info, input_path, golden_path, need_new):
81. b_value, head_num, s_value, h_value = shape_info.shape_info
82. qkv_shape = [b_value, head_num, s_value, h_value // head_num]
83. drop_shape = [b_value * head_num * s_value * s_value]
84. attention_score((qkv_shape,
85. drop_shape,
86. shape_info.keep_prob,
87. shape_info.input_dtype,
88. shape_info.output_dtype),
89. input_path,
90. golden_path,
91. need_new)
92. def get_data_file(res_path, contents):
93. data_files = {}
94. for content in contents:
95. if content["data_file"] is None:
96. continue
97. data_files[content["name"]] = os.path.join(res_path, content["data_file"])
98. return data_files
99. @dataclass
100. class InputOutputShapeInfo:
101. shape_info: tuple
102. keep_prob: int
103. input_dtype: np.dtype
104. output_dtype: np.dtype
105. def get_args():
106. """
107. 需要开发者按需配置
108. sys.argv[1]: input json file path
109. sys.argv[2]: output file path
110. sys.argv[3]: gen data type: input/output/all
111. """
112. logging.info(f"数据保存路径为: {sys.argv[2]}")
113. input_file = sys.argv[1]
114. res_path = sys.argv[2]
115. content = get_input_attrs_content(input_file)
116. input_files = get_data_file(res_path, content.get("inputs"))
117. output_files = get_data_file(res_path, content.get("outputs"))
118. attrs = content.get("attrs")
119. cmp_idx = 0
120. for attr in attrs:
121. if attr["name"] == "input_layout":
122. input_layout = attr["value"]
123. logging.info(f"get input_layout:{input_layout}")
124. if attr["name"] == "keep_prob":
125. keep_prob = attr["value"]
126. logging.info(f"get keep_prob:{keep_prob}")
127. if attr["name"] == "head_num":
128. head_num = attr["value"]
129. logging.info(f"get head_num:{head_num}")
130. shape = content.get("inputs")[cmp_idx].get("shape")
131. b_value = shape[input_layout.find("B")]
132. s_value = shape[input_layout.find("S")]
133. h_value = shape[input_layout.find("H")]
134. input_dtype = DTYPE.get(content.get("inputs")[cmp_idx].get("dtype"), np.float16)
135. output_dtype = DTYPE.get(content.get("outputs")[cmp_idx].get("dtype"), np.float16)
136. shape_info = InputOutputShapeInfo(shape_info=(b_value, head_num, s_value, h_value),
137. keep_prob=keep_prob,
138. input_dtype=input_dtype,
139. output_dtype=output_dtype)
140. return shape_info, input_files, output_files
141. if __name__ == '__main__':
142. """
143. sys.argv[1]: input data file path
144. sys.argv[2]: output file path
145. sys.argv[3]: gen data type: input/output/all
146. """
147. tensor_shape_info, input_file_list, output_file_list = get_args()
148. gen_total_golden_output(tensor_shape_info, input_file_list, output_file_list, need_new=True)
```
