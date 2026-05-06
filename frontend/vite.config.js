import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'
import axios from 'axios';

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],

   resolve: {
    alias: {
      // Force all react imports to the root node_modules version
      'react': path.resolve(__dirname, './node_modules/react'),
      'react-dom': path.resolve(__dirname, './node_modules/react-dom'),
    },
  },
})

export default {
  server: {
    proxy: {
      '/items': 'http://localhost:8000' // Target your backend server here
    }
  }
}