import CryptoJS from "crypto-js"

if (typeof window !== "undefined" && (!window.crypto || !window.crypto.subtle)) {
  // Ensure the base crypto object exists
  if (!window.crypto) {
    (window as any).crypto = {} as Crypto;
  }

  // Polyfill the minimal subset of subtle crypto that Excalidraw uses for IDs
  (window.crypto as any).subtle = {
    digest: async (algorithm: string, data: Uint8Array) => {
      if (algorithm === "SHA-256" || algorithm.toUpperCase() === "SHA-256") {
        // Convert Uint8Array to WordArray for CryptoJS
        const wordArray = CryptoJS.lib.WordArray.create(data as any);
        const hash = CryptoJS.SHA256(wordArray);
        
        // Convert back to ArrayBuffer/Uint8Array
        const hexStr = hash.toString(CryptoJS.enc.Hex);
        const typedArray = new Uint8Array(
          hexStr.match(/.{1,2}/g)!.map((byte) => parseInt(byte, 16))
        );
        return typedArray.buffer;
      }
      throw new Error(`Algorithm ${algorithm} not supported by polyfill`);
    },
    // Excalidraw sometimes checks for getRandomValues on the root crypto object
    getRandomValues: (array: Uint8Array) => {
      for (let i = 0; i < array.length; i++) {
        array[i] = Math.floor(Math.random() * 256);
      }
      return array;
    }
  };

  // Double check root fallback just in case
  if (!window.crypto.getRandomValues) {
    window.crypto.getRandomValues = (window.crypto as any).subtle.getRandomValues;
  }
}