import oneflow
from docreset import reset_docstr

reset_docstr(
    oneflow.comm.send,
    r"""send(input, dst, send_meta=True)

    同步发送张量。  

    参数：
        - **input** (tensor): 要发送的张量
        - **dst** (int): 目的地rank
        - **send_meta** (bool): 是否发送元信息（默认为 True）

    """,    
)

reset_docstr(
    oneflow.comm.recv,
    r"""recv(src, shape=None, dtype=None, device=None, *, out=None)
    
    同步接收张量。
    
    如果 send_meta = False，所有 `shape` 和 `dtype` 要有值，否则全部为 None 。

    参数：
        - **src** (int, optional): 来源 rank 。如果未指定，将从任何进程接收。
        - **shape** (optional): 输出张量形状。
        - **dataType** (optional): 输出张量数据类型。
        - **device** (optional): 输出张量设备。
        - **out** (Tensor, optional): 填充接收到的数据的张量。
    
    返回类型：
        如果 `out` 为 None，则返回接收到的张量。否则 out 将获取数据而不返回数据。

    """,
)
