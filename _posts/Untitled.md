## Define System Prompt and Configuration

This section introduces the `SYSTEM_PROMPT` and the `Configuration` class. They are essential for setting up the system’s behavior and managing environment variables (for example, choosing which language model to use). You can think of `Configuration` as the single source of truth for any settings your application might need.

## Initialize the LLM and Define the State Class

In this part, we configure the `ChatOpenAI` model (using `model` and `temperature` settings) and introduce a `State` class. The `State` class holds the conversation messages, ensuring that **context** is retained and can be easily passed around. This lays the **foundation** for a conversational agent that genuinely “remembers” what has been said.

## Write the Memory Upsert Function

Here, we focus on the `upsert_memory` function. This function is responsible for storing or updating (**upserting**) user-specific data. By preserving user context across conversations—like interests, preferences, or corrections—you can give your application a more **persistent and personalized** feel.


## Implement the Conversation Flow (call_model, store_memory)

Next, we implement two important functions for our conversation flow:

1. `call_model`: Takes the current conversation `State`, retrieves relevant memories, and then sends them along with user messages to the LLM.
2. `store_memory`: Processes the model’s **tool calls**—in this case, requests to store data—and updates the memory store accordingly.

By combining these two functions, the model not only uses past **context** but also augments it with new information in real time.


## Build and Execute the StateGraph

In this section, we construct a `StateGraph` to define the flow of the conversation. We specify which node (for instance, `call_model`) leads to which next step (for example, `store_memory`). Once the graph is set, we run sample conversations to see how the system **dynamically** manages user input, retrieves relevant memories, and updates them when necessary.


## Verify Results and View Stored Memories

Finally, we examine the stored memories to confirm that our system has correctly captured the user’s context. You can look into the final conversation state (using `graph.get_state`) and see how messages and memories have been organized. This is a great point to do some **debugging** if anything seems amiss, ensuring that your memory mechanism works just as intended.



