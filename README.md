# hello-web

The tiny web app used in the [Maritime docs](https://maritime.sh/docs/cli) to demo
deploying your own code to a public URL:

```bash
maritime create hello-web --repo https://github.com/mariagorskikh/maritime-hello-web --public
```

One Python file, standard library only. It listens on `$PORT` (injected by the
platform at runtime) and answers every GET with a small JSON payload.
