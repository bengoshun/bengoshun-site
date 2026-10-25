export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    // 旧URL（*.workers.dev）へのアクセスは独自ドメインへ301転送
    if (url.hostname.endsWith(".workers.dev")) {
      url.hostname = "bengoshun.com";
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(request);
  },
};
