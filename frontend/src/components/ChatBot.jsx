"use client";

import React, { useEffect, useState, useRef } from "react";
import WebSocket from "isomorphic-ws";

const ChatBot = () => {
  const [messages, setMessages] = useState([
    { from: "bot", text: "Hello 👋 I'm BRIGHTBOT. How can I assist you?" },
  ]);
  const [input, setInput] = useState("");
  const wsRef = useRef(null);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    wsRef.current = new WebSocket("ws://localhost:8000/web-socket/chat/");

    wsRef.current.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        setMessages((prev) => [...prev, { from: "bot", text: data.response }]);
      } catch (err) {
        console.error("WebSocket JSON parse error:", event.data);
      }
    };

    wsRef.current.onerror = (error) => {
      console.error("WebSocket error:", error);
    };

    wsRef.current.onclose = () => {
      console.log("WebSocket closed");
    };

    return () => wsRef.current.close();
  }, []);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = () => {
    if (input.trim() === "") return;
    setMessages((prev) => [...prev, { from: "user", text: input }]);
    wsRef.current.send(JSON.stringify({ message: input }));
    setInput("");
  };

  return (
    <div className="max-w-2xl mx-auto mt-8 p-6 bg-gray-900 text-white rounded-2xl shadow-2xl border border-gray-800">
      <h2 className="text-2xl font-bold text-center mb-6 text-indigo-400">
        💬 BrightBot Chat
      </h2>

      <div className="h-96 overflow-y-auto bg-gray-800 rounded-lg p-4 space-y-4 border border-gray-700">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`flex ${
              msg.from === "user" ? "justify-end" : "justify-start"
            }`}
          >
            <span
              className={`px-4 py-2 rounded-2xl max-w-[75%] text-sm sm:text-base ${
                msg.from === "user"
                  ? "bg-indigo-600 text-white"
                  : "bg-gray-700 text-gray-100"
              }`}
            >
              {msg.text}
            </span>
          </div>
        ))}
        <div ref={messagesEndRef}></div>
      </div>

      <div className="mt-4 flex items-center gap-2">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          placeholder="Type your message..."
          className="flex-1 px-4 py-3 rounded-full bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-500 placeholder-gray-400"
        />
        <button
          onClick={sendMessage}
          disabled={!input.trim()}
          className="px-5 py-3 bg-indigo-600 hover:bg-indigo-700 rounded-full text-white font-semibold transition duration-200 disabled:opacity-50"
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatBot;
