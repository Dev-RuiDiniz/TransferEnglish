from typing import List, Dict, Any
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

class ChatService:
    def __init__(self, model: str = "gpt-4o"):
        self.llm = ChatOpenAI(model=model, temperature=0.7)
        self.system_prompt = (
            "You are a specialized English tutor for Portuguese speakers. "
            "Your goal is to achieve functional fluency in 6 months using Linguistic Transfer. "
            "Focus on using cognates (words similar in PT and EN) to build student confidence. "
            "Always respond in English, but use simple structures at first. "
            "If the student makes a phonetic error or uses a false cognate, gently guide them. "
            "Keep responses short and conversational, suitable for audio interaction."
        )

    async def get_response(self, history: List[Dict[str, str]], user_input: str) -> str:
        messages = [SystemMessage(content=self.system_prompt)]
        
        # Add history
        for msg in history:
            if msg["role"] == "user":
                messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                messages.append(AIMessage(content=msg["content"]))
        
        # Add current user input
        messages.append(HumanMessage(content=user_input))
        
        response = await self.llm.ainvoke(messages)
        return response.content

chat_service = ChatService()
