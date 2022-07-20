import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Price Tracker</title>
        <meta name="description" content="Small application for price tracking of Suppermarkets in Paraguay." />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <center>
          <h1>Price Tracker</h1>
        </center>
      </main>

    </div>
  )
}
