"use client";

import "../utils/crypto-polyfill"; 

import React, { useState } from "react";
import { Excalidraw } from "@excalidraw/excalidraw";
import "@excalidraw/excalidraw/index.css";

export default function ExcalidrawWrapper() {
  const [excalidrawAPI, setExcalidrawAPI] = useState<any>(null);
  const UIOptions = {
    canvasActions: {
      changeViewBackgroundColor: false,
      clearCanvas: false,
      loadScene: false,
      toggleTheme: false,
      export: false
    },
  };

  return (
    // Rule: Excalidraw expands to fill 100% of its parent wrapper.
    // If your container has a height of 0, the canvas will look invisible!
    <div className="w-screen h-screen relative">
      <Excalidraw 
        UIOptions = {UIOptions},
        theme="dark" // Forces dark mode
      />
    </div>
  );
}``