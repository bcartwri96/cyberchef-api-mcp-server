# CyberChef API MCP Server

This model context protocol (MCP) server interfaces with the [CyberChef Server](https://github.com/gchq/CyberChef-server) API. Allowing you to use any LLM/MCP client of your choosing to utilise the tools and resources within CyberChef.

Usage
---
Start the server using the default stdio transport and specifying an environment variable pointing to a CyberChef API

```bash
CYBERCHEF_API_URL="your-cyberchef-api-url" uv run cyberchef_api_mcp_server
```

Usage (Development)
---
Start the server and test it with the MCP inspector

```bash
uv add "mcp[cli]"
mcp dev server.py
```

Example Use Case
---
Using the MCP server in this example use case, the following prerequisites apply: 
- You must have Claude desktop installed
- Have a running CyberChef API instance or one you are able to use

```bash
uv add "mcp[cli]"
mcp install server.py --name "CyberChef API MCP Server"
```

> [!TIP]
> After running the above command you can then tweak the Claude client configuration to include the environment variable for the CyberChef API URL

```json
{
 "mcpServers": {
   "elasticsearch-mcp-server": {
     "command": "uv",
     "args": [
       "run",
       "--with",
       "mcp[cli]",
       "--directory",
       "cyberchef-api-mcp-server/cyberchef_api_mcp_server/",
       "mcp",
       "run",
       "server.py"
     ],
     "env": {
       "CYBERCHEF_API_URL": "your-cyberchef-api-url"
     }
   }
 }
}
```

Here is a basic prompt being solved using the MCP server tools:
<img width="1511" src="https://github.com/user-attachments/assets/657f52b3-43eb-4c3b-94f1-289fc12817b2" />

License
---
MIT License
