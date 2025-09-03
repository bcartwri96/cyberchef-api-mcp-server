from openai import OpenAI
import os
import dotenv

url = 'https://secure-alpaca-extremely.ngrok-free.app'

with open("./encoded_layers.txt", "r") as f:
	file_enc = f.read()

print(file_enc)
dotenv.load_dotenv("cyberchef_api_mcp_server/key.env")

client = OpenAI()

resp = client.responses.create(
    model="gpt-5-nano",
    tools=[
        {
            "type": "mcp",
            "server_label": "cyberchef",
            "server_url": f"{url}/mcp",
            "require_approval": "never",
        },
    ],
    input=f"decode this using cyberchef tool and show working: {file_enc}",
    #input="decode this - only try once. if you fail initially, report back findings: UEsDBBQAAAAIAEqZI1uFEUoNFwAAAAsAAAAIAAAAZmlsZS50eHQFgEEJAAAIxKoYTsHH4MCP9ccOpD5HC1BLAQIUABQAAAAIAEqZI1uFEUoNFwAAAAsAAAAIAAAAAAAAAAAAAAAAAAAAAABmaWxlLnR4dFBLBQYAAAAAAQABADYAAAA9AAAAAAA= and show me the output.",
)

print(resp.output_text)
