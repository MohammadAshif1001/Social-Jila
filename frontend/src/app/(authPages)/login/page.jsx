"use client";
import React from "react";
import { useSession, signIn, singOut } from "next-auth/react";

const login = () => {
  const { data: session } = useSession();

  if (session) {
    return (
      <>
        Signed in as {session.user.email}
        <br />
        <button onClick={() => singOut()}>Sign out</button>
      </>
    );
  }
  return (
    <>
      Signed in as {session.user.email}
      <br />
      <button onClick={() => signIn()}>Sign in</button>
    </>
  );
};

export default login;
