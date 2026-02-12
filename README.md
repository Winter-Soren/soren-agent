# Soren Agent 🤖

A production-ready, extensible AI agent framework built with Python that enables autonomous task execution through a sophisticated tool system, MCP integration, and advanced safety controls.

## Overview

Soren Agent is a powerful agentic AI framework designed for developers who need reliable, safe, and extensible AI automation. It combines streaming LLM responses with a robust tool execution system, comprehensive safety policies, and seamless integration with the Model Context Protocol (MCP) ecosystem.

## Key Features

### Core Capabilities

- **Dual Execution Modes**: Run interactively in a rich TUI or execute single commands programmatically
- **Streaming Responses**: Real-time text streaming with token-by-token output
- **Multi-Turn Conversations**: Maintains context across multiple interactions with intelligent compression
- **Agentic Loop**: Autonomous tool calling with configurable turn limits and loop detection
- **Event-Driven Architecture**: Comprehensive event system for monitoring agent lifecycle and tool execution

### Built-in Tool Suite

The framework includes a comprehensive set of built-in tools:

- **File Operations**: `read_file`, `write_file`, `edit_file` - Full file manipulation capabilities
- **Directory Management**: `list_dir`, `glob` - Navigate and search filesystem
- **Text Search**: `grep` - Powerful pattern matching across files
- **Shell Execution**: `shell` - Execute system commands with safety controls
- **Web Access**: `web_search`, `web_fetch` - Search and retrieve web content
- **Memory System**: `memory` - Persistent key-value storage for agent preferences
- **Task Management**: `todo` - Built-in task tracking

### Intelligent Context Management

- **Automatic Compression**: Intelligently compresses conversation history when approaching token limits
- **Smart Pruning**: Removes old tool outputs to maintain context efficiency
- **Token Tracking**: Real-time monitoring of token usage across conversations
- **Configurable Windows**: Support for models with different context window sizes

### Advanced Safety & Approval System

Multiple approval policies to match your security requirements:

- `on-request`: Prompt for confirmation on mutating operations (default)
- `auto`: Automatically approve safe operations, prompt for dangerous ones
- `never`: Block all mutating operations
- `yolo`: Auto-approve everything (use with caution!)

Safety features include:
- Dangerous command detection (rm -rf, format, etc.)
- Path-based safety checks
- Configurable shell environment policies
- Environment variable filtering

### Session Management

- **Persistent Sessions**: Save and resume conversations with full context
- **Checkpoints**: Create restore points during long-running tasks
- **Session History**: Browse and manage multiple saved sessions
- **Metadata Tracking**: Automatic tracking of turns, timestamps, and token usage

### Model Context Protocol (MCP) Integration

Seamlessly integrate with the MCP ecosystem:

- **Multiple Transports**: Support for stdio and HTTP/SSE connections
- **Dynamic Tool Loading**: Automatically discover and register MCP server tools
- **Server Management**: Monitor connection status and available tools
- **Configurable Servers**: Define multiple MCP servers with custom environments

Example MCP configuration:
```toml
[mcp_servers.filesystem]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/workspace"]

[mcp_servers.database]
url = "http://localhost:3000/mcp"
```

### Subagent System

Delegate specialized tasks to purpose-built subagents:

- **Codebase Investigator**: Analyzes code structure and dependencies
- **Code Reviewer**: Performs automated code reviews
- **Custom Subagents**: Define your own with specific tools and constraints

### Loop Detection

Prevents infinite loops and repetitive behavior:

- Detects repeated tool calls with identical parameters
- Identifies circular reasoning patterns
- Automatically injects loop-breaking prompts
- Configurable detection thresholds

### Hooks System

Execute custom logic at key points in the agent lifecycle:

```toml
[[hooks]]
name = "lint_on_write"
trigger = "after_tool"
command = "npm run lint"
timeout_sec = 30
```

Supported triggers:
- `before_agent` / `after_agent`: Around agent execution
- `before_tool` / `after_tool`: Around tool calls
- `on_error`: When errors occur

### Flexible Configuration

Configure via `.soren/config.toml`:

```toml
hooks_enabled = true

[model]
name = "openai/gpt-4o-mini"
temperature = 0.7

[mcp_servers.filesystem]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-filesystem", "/workspace"]
```

Configuration options:
- Model selection and parameters
- Working directory
- Tool allowlisting
- Developer/user instructions
- Shell environment policies
- MCP server definitions
- Hook configurations

### Rich Terminal UI

Beautiful, informative terminal interface:

- Color-coded output for different event types
- Real-time tool execution visualization
- Diff display for file modifications
- Token usage statistics
- Progress indicators

### Interactive Commands

Powerful command interface for session control:

- `/help` - Show available commands
- `/config` - Display current configuration
- `/model <name>` - Switch LLM model
- `/approval <policy>` - Change approval policy
- `/tools` - List available tools
- `/mcp` - Show MCP server status
- `/stats` - Display session statistics
- `/save` - Save current session
- `/resume <id>` - Resume saved session
- `/checkpoint` - Create restore point
- `/restore <id>` - Restore from checkpoint
- `/clear` - Clear conversation history
- `/exit` - Quit the agent

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- OpenRouter API key (or compatible LLM provider)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd soren-agent
```

2. Install dependencies using uv:
```bash
uv sync
```

3. Set up environment variables:
```bash
# Create .env file
echo "OPENROUTER_API_KEY=your_api_key_here" > .env
echo "OPENROUTER_BASE_URL=https://openrouter.ai/api/v1" >> .env
```

4. Configure the agent:
```bash
# Edit .soren/config.toml with your preferences
```

### Usage

**Interactive Mode:**
```bash
python main.py
```

**Single Command Mode:**
```bash
python main.py "Analyze the codebase and create a summary"
```

**Custom Working Directory:**
```bash
python main.py --cwd /path/to/project "List all Python files"
```

## Project Structure

```
soren-agent/
├── agent/              # Core agent implementation
│   ├── agent.py       # Main agent loop and orchestration
│   ├── session.py     # Session management and state
│   ├── events.py      # Event system definitions
│   └── persistence.py # Session persistence
├── client/            # LLM client abstraction
│   ├── llm_client.py  # OpenAI-compatible client
│   └── response.py    # Response parsing and streaming
├── config/            # Configuration management
│   ├── config.py      # Configuration models
│   └── loader.py      # Config loading and validation
├── contexts/          # Context management
│   ├── manager.py     # Message history management
│   ├── compaction.py  # Context compression
│   └── loop_detector.py # Loop detection logic
├── hooks/             # Hook system
│   └── hook_system.py # Hook execution engine
├── safety/            # Safety and approval
│   └── approval.py    # Approval policies and checks
├── tools/             # Tool system
│   ├── base.py        # Tool base classes
│   ├── registry.py    # Tool registration and invocation
│   ├── discovery.py   # Dynamic tool discovery
│   ├── subagents.py   # Subagent definitions
│   ├── builtin/       # Built-in tools
│   └── mcp/           # MCP integration
│       ├── client.py  # MCP client implementation
│       ├── mcp_manager.py # MCP server management
│       └── mcp_tool.py    # MCP tool wrapper
├── ui/                # User interface
│   └── tui.py         # Terminal UI implementation
├── utils/             # Utilities
│   ├── errors.py      # Error definitions
│   ├── paths.py       # Path utilities
│   └── text.py        # Text processing
└── main.py            # Entry point
```

## Advanced Usage

### Creating Custom Tools

```python
from tools.base import Tool, ToolInvocation, ToolResult, ToolKind
from pydantic import BaseModel

class MyToolParams(BaseModel):
    input: str

class MyCustomTool(Tool):
    name = "my_tool"
    description = "Does something useful"
    kind = ToolKind.READ
    schema = MyToolParams
    
    async def execute(self, invocation: ToolInvocation) -> ToolResult:
        params = MyToolParams(**invocation.params)
        # Your logic here
        return ToolResult.success_result("Done!")
```

### Defining Subagents

```python
from tools.subagents import SubagentDefinition

custom_subagent = SubagentDefinition(
    name="my_subagent",
    description="Specialized task handler",
    instructions="You are an expert at...",
    allowed_tools=["read_file", "write_file"],
    max_turns=10
)
```

### Custom Hooks

```toml
[[hooks]]
name = "security_scan"
trigger = "before_tool"
command = "python security_check.py"
timeout_sec = 15
enabled = true
```

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## Acknowledgments

- Built with [OpenAI API](https://openai.com) compatibility
- Supports [OpenRouter](https://openrouter.ai) for multi-model access
- Integrates with [Model Context Protocol](https://modelcontextprotocol.io)
- UI powered by [Rich](https://rich.readthedocs.io)

