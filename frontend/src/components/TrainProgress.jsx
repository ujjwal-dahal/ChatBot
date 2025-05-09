// components/TrainProgress.js
"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export default function TrainProgress() {
  const [progress, setProgress] = useState(0);
  const router = useRouter();

  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8000/ws/train/");

    socket.onopen = () => {
      socket.send(JSON.stringify({ message: "start_training" }));
    };

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.percent !== undefined) {
        setProgress(data.percent);
        if (data.percent === 100) {
          setTimeout(() => {
            router.push("/chatbot");
          }, 2000);
        }
      }
    };

    return () => socket.close();
  }, []);

  return (
    <div className="mt-6 text-white">
      <p>Training Progress: {progress}%</p>
      <progress value={progress} max="100" className="w-full h-4 rounded" />
    </div>
  );
}
