import { CircularProgress, Paper, Typography } from "@mui/material";

import { useEffect, useState } from "react";

import { sendRequest } from "../../../utility";
import * as config from "../../../config";

import classes from "./AccountDetails.module.css";
import AccountDetailsForm from "./AccountDetailsForm/AccountDetailsForm";
import AccountDetailsAuthForm from "./AccountDetailsAuthForm/AccountDetailsAuthForm";
import ChangePasswordForm from "./ChangePasswordForm/ChangePasswordForm";
import DeleteAccountForm from "./DeleteAccountForm/DeleteAccountForm";
import ChangeEmailForm from "./ChangeEmailForm/ChangeEmailForm";
import EmailUpdateSuccess from "./EmailUpdateSuccess/EmailUpdateSuccess";
import DeleteAccountSuccess from "./DeleteAccountSuccess/DeleteAccountSuccess";

const ErrorMessage = () => {
  return (
    <div className={classes.error}>
      <p>Server connection Error: please check your internet connection</p>
      <p>If the issue continues to occur, contact our help centre</p>
    </div>
  );
};

const AccountDetails = () => {
  const [page, setPage] = useState("auth");
  const [isLoading, setIsLoading] = useState(false);
  const [details, setDetails] = useState({
    username: "",
    firstname: "",
    lastname: "",
  });

  useEffect(() => {
    const fetchData = async () => {
      const authToken = localStorage.getItem("parkItAuthToken");
      if (!authToken) return;

      try {
        const url = `${config.SERVER_URL}/api/auth/user/`;
        const options = {
          method: "GET",
          headers: {
            Authorization: "Bearer " + authToken,
          },
        };
        const response = await sendRequest(url, options, setIsLoading);
        if (response.status >= 300 || !response.status) throw Error;
        setDetails(response.data);
      } catch (e) {
        setPage("error");
      }
    };

    if (page === "details") fetchData();
  }, [page]);

  // prettier-ignore
  return (
    <>
      <Typography variant="sectionTitle">Account Details</Typography>
      <Paper elevation={0} className={classes.body}>
        {isLoading && <CircularProgress className={classes.spinner} size="3rem"/>}
        {page === "error" && <ErrorMessage />}
        {page === "auth" && <AccountDetailsAuthForm setPage={setPage} />}
        {page === "details" && <AccountDetailsForm details={details} setPage={setPage}/>}
        {page === "changePassword" && <ChangePasswordForm setPage={setPage}/>}
        {page === "changeEmail" && <ChangeEmailForm setPage={setPage}/>}
        {page === "emailUpdateSuccess" && <EmailUpdateSuccess setPage={setPage}/>}
        {page === "deleteAccount" && <DeleteAccountForm setPage={setPage}/>}
        {page === "deleteAccountSuccess" && <DeleteAccountSuccess setPage={setPage}/>}
      </Paper>
    </>
  );
};

export default AccountDetails;
