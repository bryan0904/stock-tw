# 1. Build 階段：用 Node.js 編譯 React
FROM node:16 AS build
WORKDIR /app

# 複製 package.json & package-lock.json（有就用，沒有也不會出錯）
COPY package*.json ./

# 安裝依賴（npm install 可兼容有/無 lockfile）
RUN npm install

# 複製其餘原始碼並編譯
COPY . .
RUN npm run build

# 2. Serve 階段：用 Nginx 服務靜態檔
FROM nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
