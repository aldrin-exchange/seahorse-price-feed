# seahorse-price-feed
A simple Seahorse program that retrieves prices from the [Pyth network](https://pyth.network/) oracle.

## Tutorial

Follow the steps below to run and test this smart contract.

1. From the command line run `seahorse init pricefeed` to start a new project called pricefeed.

2. Replace the generated `pricefeed.py` file in `pricefeed/programs_py` with the `pricefeed.py` file of this repository.

3. Go to the `pricefeed` folder and run `seahorse build`.

4. Now we need to obtain the public key of our program. Execute (from the `pricefeed` folder) the command

`solana-keygen pubkey target/deploy/pricefeedtest-keypair.json`

5. Copy the public key shown and insert it in the `declare_id` command of the `pricefeed.py` file.

6. Build the program again with `seahorse build`.

**Remark:** Steps 5 and 6 are important because we will deploy the program from the Solana Playground, so we need it to be ready. Of course, it can be also deployed from the command line with `anchor deploy`, but in this example we prefer to do it using the Solana Playground for educational purposes.

7. Now go to the [Solana Playground](https://beta.solpg.io/).

8. Check that you are connected to devnet.

9. Click on the hammer and wrench icon. :hammer_and_wrench:

10. In the `Upload a program` menu upload the `pricefeed.so` file that is located on `pricefeed/target/deploy`.

11. Now we will import the `Program credentials`. Click on the `Import` button and choose the `pricefeed-keypair.json` file that is located on `pricefeed/target/deploy`.

12. You will see that the program id appears. It should be the same public key as the one we copied in step 5.

13. Finally, go to the `IDL` menu. Click on `Import` and choose the `pricefeed.json` file that is located on `pricefeed/target/idl`.

14. Now click on `Deploy`. This will deploy the program to devnet.

### Tests:

We will now interact with our smart contract.

15. We will first run the `getSolUsdPrice` instruction. In the `priceAccount` field we write the public key of the devnet account that tracks the price of the SOL/USD pair. This public key is `J83w4HKfqxwcq3BEMMkPFSppX3gqekLyLJBexebFVkix` and can be found [here](https://pyth.network/price-feeds/crypto-sol-usd?cluster=devnet).

16. We now run the `getEthUsdPrice` instruction. In the `priceAccount` field we write the public key of the devnet account that tracks the price of the ETH/USD pair. This public key is `EdVCmQ9FSPcVe5YySXDPCRmc8aDQLKJ9xvYBMZPie1Vw` and can be found [here](https://pyth.network/price-feeds/crypto-eth-usd?cluster=devnet).

17. Now we will execute the `solNetWorth` instruction, which computes the value in USD of a certain amount of SOL. In the `balance` field we write the amount of SOL and in the `priceAccount` field we write the public key of the devnet account that tracks the price of the SOL/USD pair (which is `J83w4HKfqxwcq3BEMMkPFSppX3gqekLyLJBexebFVkix`).

The results of these instructions are logged in the Solana devnet.
