export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    // 旧URL（*.workers.dev）と www 付きは bengoshun.com へ301転送し、評価の分散を防ぐ
    if (url.hostname.endsWith(".workers.dev") || url.hostname === "www.bengoshun.com") {
      url.hostname = "bengoshun.com";
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(request);
  },
};
