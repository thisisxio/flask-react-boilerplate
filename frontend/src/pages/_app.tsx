import { AppProps } from "next/dist/shared/lib/router/router";
import RootLayout from "../components/layout";

export default function App({ Component, pageProps }: AppProps) {
  return (
    <RootLayout>
      <Component {...pageProps} />
    </RootLayout>
  );
}
