from mcp_factory.server import mcp

# 工具：跟朋友们打个招呼
@mcp.tool(
    name="GreetingToFriends",
    description="跟朋友们打个招呼",
    tags={"社交", "工具"}
)
def greeting_to_friends(greeter: str) -> str:
    """跟朋友们打个招呼"""
    # 待办事项：在这里实现您的业务逻辑
    print(f"参数 greeter: {greeter}")
    return f"您好, {greeter}！"
