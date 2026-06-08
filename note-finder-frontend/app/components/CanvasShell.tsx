"use client";

import dynamic from "next/dynamic";

const ExcalidrawCanvas = dynamic(
  () => import("./ExcalidrawWrapper"), // Adjust path if needed
  { ssr: false }
);

export default function CanvasShell() {
  return <ExcalidrawCanvas />;
}