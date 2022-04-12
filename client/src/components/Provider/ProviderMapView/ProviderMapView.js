import classes from "./ProviderMapView.module.css";
import { Link, useLocation } from "react-router-dom";
import { useContext, useEffect, useState } from "react";

import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import { Scrollbars } from 'react-custom-scrollbars-2';
import {
    Button,
    Tab,
    Tabs,
    Typography,
    Divider,
    CircularProgress,
} from "@mui/material";

// React Icon import
import ListAltIcon from '@mui/icons-material/ListAlt';
import MapIcon from '@mui/icons-material/Map';
import BeenhereIcon from '@mui/icons-material/Beenhere';
import ArchiveIcon from '@mui/icons-material/Archive';


import { sendRequest } from "../../../utility";
import * as config from "../../../config";
import ProviderMapItem from "./ProviderMapItem";
import CarSpaceModalContext from "../../../contexts/carspace-modal-context";

const ProviderMapView = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState({ value: false, message: ""});
    const [carSpaces, setCarSpaces] = useState([]);
    const carSpaceModalContext = useContext(CarSpaceModalContext);

    const location = useLocation();
    const activeTabView = location.pathname.split("/")[2] ?? false;
    const activeTabListings = location.pathname.split("/")[3] ?? false;
    // prettier-ignore
    const pendingUrl = `${location.pathname.split("/").slice(0, 3).join("/")}/pending`;
    // prettier-ignore
    const activeUrl = `${location.pathname.split("/").slice(0, 3).join("/")}/active`;
    
    const addCarSpaceHandler = () => {
        carSpaceModalContext.openPage("/add");
    };

    useEffect(() => {
        const fetchData = async () => {
          try {
            const authToken = localStorage.getItem("parkItAuthToken");
            const url = `${
            config.SERVER_URL
            }/api/provider/parking/all`;
            const options = {
            method: "GET",
            headers: {
                Authorization: "Bearer " + authToken,
                "Content-Type": "application/json",
            },
            };

            const response = await sendRequest(url, options, setIsLoading);
            if (response.status >= 300 || !response.status) throw Error;
            
            console.log(response.data);
            setCarSpaces(response.data);
          } catch (e) {
            setError({
              value: true,
              message: config.NETWORK_ERROR_MESSAGE,
            });
          }
        };
    
        fetchData();
    }, [carSpaceModalContext.carSpacesRefreshStatus]);
    
    return (
    <div className={classes.bodyContainer}>
        <div className={classes.menuContainer}>
            <Typography
                variant="modalTitle"
                className={classes.title}
                color="textSecondary"
                fontWeight="Bold"
            > Your Car Spaces </Typography>
            <div className={classes.viewSelection}>
                <Tabs
                    value={activeTabView}
                    orientation="horizontal"
                    className={classes.tabContainer}
                >
                    <Tab
                        className={classes.menu__tab}
                        component={Link}
                        to="/provider/mapView/active"
                        value="mapView"
                        label="Map"
                        icon={<MapIcon className={classes["tab-icon"]} />}
                        iconPosition="start"
                    />
                    <Tab
                        className={classes.menu__tab}
                        component={Link}
                        to="/provider/listView/active"
                        value="listView"
                        label="List"
                        icon={<ListAltIcon className={classes["tab-icon"]} />}
                        iconPosition="start"
                    />
                </Tabs>
                <Divider orientation="vertical" variant="middle" className={classes.navbar_divider_betweenTabs} />
                <Tabs
                    value={activeTabListings}
                    orientation="horizontal"
                    className={classes.tabContainer}
                    variant="scrollable"
                    scrollButtons={false}
                >
                    <Tab
                        className={classes.menu__tab}
                        component={Link}
                        to={activeUrl}
                        value="active"
                        label="active"
                        icon={<BeenhereIcon className={classes["tab-icon"]} />}
                        iconPosition="start"
                    />
                    <Tab
                        className={classes.menu__tab}
                        component={Link}
                        to={pendingUrl}
                        value="pending"
                        label="pending"
                        icon={<ArchiveIcon className={classes["tab-icon"]} />}
                        iconPosition="start"
                    />
                </Tabs>
            </div>
            <div className={classes.listingContainer}>
            <Divider orientation="horizontal" className={classes.navbar_divider_listingStart} />
            <Scrollbars
                renderView={props => (
                    <div {...props} style={{ ...props.style, 
                        overflowX: 'hidden',
                        height: '100%',
                        display: 'flex',
                        flexDirection: 'column',
                        alignItems: 'center',
                    }}/>
                )}
                renderTrackHorizontal={props => <div {...props} style={{display: 'none'}} className="view"/>}
            >
                {isLoading && (
                    <div className={classes.center_container}>
                        <CircularProgress className={classes.spinner} />
                    </div>
                )}
                {!isLoading &&
                    !error.value &&
                    carSpaces.map((item) => (
                        <ProviderMapItem
                            key={item.pk}
                            id={item.pk}
                            streetAddress={item.streetAddress}
                            notes={item.notes}
                            size={item.size}
                            price={item.price}
                            image={item.images[0].image_data}
                        />
                    ))
                }
                {!isLoading 
                    && error.value 
                    && (
                        <div className={classes.center_container}>{error.message}</div>
                    )
                }
            </Scrollbars>
            </div>
        </div>
        <div className={classes.mapContainer}>
            <MapContainer 
                className={classes.mapElement}
                center={[-33.916663, 151.2420]} 
                zoom={16} 
                scrollWheelZoom={true}
                dragging={true}
                animate={true}
                easeLinearity={0.35}>
                <TileLayer
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                <Marker position={[-33.916663, 151.2420]}>
                    <Popup>
                        Welcome to BMG HQ
                    </Popup>
                </Marker>
            </MapContainer>
            <Button
                color="primary"
                variant="contained"
                size="large"
                onClick={addCarSpaceHandler}
            ></Button>
        </div>
   </div>
  )
};

export default ProviderMapView;




